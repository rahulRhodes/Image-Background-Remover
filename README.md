

---

## 📑 State of the Art Review  
📄 [Read the full review here](https://docs.google.com/document/d/1okXH0WwAznkjQCDh_ZY9uRtl9u5aocl5/edit?usp=drive_link&ouid=107960887514237623929&rtpof=true&sd=true).

---
🖼️ Background Remover API

A simple FastAPI application to remove image backgrounds using the rembg
 library.
Supports both image URLs and file uploads.

✨ Features

🟢 Remove background from an image URL.

🔵 Remove background from an uploaded file.

🗂️ Saves processed images into an outputs/ folder.

🌐 Serves processed images via a local static URL.

⚙️ Installation

Clone the repository and install dependencies:

git clone https://github.com/your-username/background-remover-api.git
cd background-remover-api

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

# Install requirements
pip install -r requirements.txt

▶️ Run the API

Start the FastAPI server with Uvicorn:

uvicorn main:app --reload


API will be available at:
👉 http://127.0.0.1:8000/docs
 (Swagger UI)

🔌 API Endpoints
1️⃣ Remove BG from Image URL

Endpoint:

POST /remove_bg


Body (JSON):

{
  "img_url": "https://example.com/sample.jpg"
}


Response:

{
  "rmv_img_url": "http://127.0.0.1:8000/outputs/AbCdEfGhIj.png"
}

2️⃣ Remove BG from Uploaded File

Endpoint:

POST /remove_bg_upload


Form Data:

file → Upload an image file (JPG, PNG, etc.)

Response:

{
  "rmv_img_url": "http://127.0.0.1:8000/outputs/XyZpQrLmNo.png"
}

📂 Project Structure
.
├── main.py             # FastAPI app
├── requirements.txt    # Dependencies
├── outputs/            # Processed images (auto-created)
└── README.md           # Documentation

🛠️ Tech Stack

FastAPI
 – API framework

Rembg
 – Background removal

OpenCV
 – Image processing

NumPy
 – Array operations
