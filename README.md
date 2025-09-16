# 🖼️ Image Background Removal API  

This repository demonstrates an **end-to-end pipeline** for serving an **image background removal model** via an API deployed on AWS.

---

## 📑 State of the Art Review  
📄 [Read the full review here](https://docs.google.com/document/d/1okXH0WwAznkjQCDh_ZY9uRtl9u5aocl5/edit?usp=drive_link&ouid=107960887514237623929&rtpof=true&sd=true).

---

## 🧩 Background Removal  

We use the [**rembg**](https://github.com/danielgatis/rembg) library for background removal.  

### 🔹 Installation  
```bash
pip install rembg



from rembg import remove

input_path = 'input.png'
output_path = 'output.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)



API Deployment

The API is deployed on an AWS EC2 (t2.2xlarge) instance.

🔹 Setup EC2 Instance

Log into AWS and create an EC2 instance with Ubuntu (latest LTS).

SSH into the instance and run:

sudo apt-get update
sudo apt install -y python3-pip nginx

🔹 Configure NGINX
sudo nano /etc/nginx/sites-enabled/fastapi_nginx


Paste the following (replace <YOUR_EC2_IP> with your instance public IP):

server {
    listen 80;
    server_name <YOUR_EC2_IP>;

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}


Restart NGINX:

sudo service nginx restart


👉 Update your EC2 security group to allow inbound traffic on port 80 (HTTP).

🚀 Serve Background Removal via API

Clone this repository:

git clone https://github.com/rahulRhodes/Image-Background-Remover.git
cd image-background-removal-api-end-to-end-pipeline

🔹 Setup Virtual Environment
sudo apt install python3-virtualenv

virtualenv venv --python=python3
source venv/bin/activate

pip install -r requirements.txt

🔹 Launch FastAPI App
python3 -m uvicorn main:app

