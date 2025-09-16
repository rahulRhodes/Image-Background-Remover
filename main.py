# import os
# import random
# import string
# import urllib

# import boto3
# import rembg
# import cv2
# from fastapi import FastAPI

# import awscredentials


# client = boto3.client(
#                         's3',
#                         aws_access_key_id=awscredentials.access_key,
#                         aws_secret_access_key=awscredentials.secret_key
#                         )

# bucket_name = None


# app = FastAPI()


# @app.post("/remove_bg")
# async def remove_bg(img_url):

#     filename = ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase) for j in range(10)]) + '.png'

#     urllib.request.urlretrieve(img_url, filename)

#     img = cv2.imread(filename)

#     output = rembg.remove(img)

#     cv2.imwrite(filename, output)

#     client.upload_file(filename, bucket_name, filename)

#     os.remove(filename)

#     return {"rmv_img_url": 'https://{}.s3.amazonaws.com/{}'.format(bucket_name, filename)}


import os
import random
import string
import urllib

import rembg
import cv2
import numpy as np
from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles

# Output folder for processed images
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

app = FastAPI()

# Mount the outputs folder so it can be served at /outputs/
app.mount("/outputs", StaticFiles(directory=OUTPUT_DIR), name="outputs")

def generate_filename(ext=".png"):
    return ''.join(
        [random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(10)]
    ) + ext

# --- Endpoint 1: Remove BG from image URL ---
@app.post("/remove_bg")
async def remove_bg(img_url: str):
    filename = generate_filename(".png")

    # Download input image
    urllib.request.urlretrieve(img_url, filename)

    # Read image
    img = cv2.imread(filename)

    # Remove background
    output = rembg.remove(img)

    # Save output into outputs/ folder
    output_path = os.path.join(OUTPUT_DIR, filename)
    cv2.imwrite(output_path, output)

    # Delete temporary downloaded input file
    os.remove(filename)

    # Return a local URL (served via StaticFiles)
    rmv_img_url = f"http://127.0.0.1:8000/outputs/{filename}"
    return {"rmv_img_url": rmv_img_url}


# --- Endpoint 2: Remove BG from uploaded file ---
@app.post("/remove_bg_upload")
async def remove_bg_upload(file: UploadFile = File(...)):
    # Create random filename with same extension as upload
    _, ext = os.path.splitext(file.filename)
    filename = generate_filename(ext if ext else ".png")

    # Read uploaded file into memory
    file_bytes = await file.read()
    nparr = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

    # Remove background
    output = rembg.remove(img)

    # Save output
    output_path = os.path.join(OUTPUT_DIR, filename)
    cv2.imwrite(output_path, output)

    # Return local URL
    rmv_img_url = f"http://127.0.0.1:8000/outputs/{filename}"
    return {"rmv_img_url": rmv_img_url}
