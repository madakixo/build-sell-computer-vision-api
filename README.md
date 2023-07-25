# build-sell-computer-vision-api

<p align="center">
<a href="https://www.youtube.com/watch?v=Dc_FaAziNxI">
    <img width="600" src="https://utils-computervisiondeveloper.s3.amazonaws.com/thumbnails/with_play_button/build_sell_api.jpg" alt="Watch the video">
    </br>Watch on YouTube: Build and sell your own computer vision API | <br> Image classification with Python and Yolov8
</a>
</p>

## model

We will be using an image classifier I trained with Yolov8. The model was trained using [this dataset](https://www.kaggle.com/datasets/rhammell/ships-in-satellite-imagery) and following [this step by step tutorial on how to train an image classifier with Yolov8 on your custom data](https://youtu.be/ZeLg5rxLGLg). The model is available [here](https://drive.google.com/file/d/1n0Go3IvpESXUmyGidyx6RakFmTMjKjLJ/view?usp=sharing).

### model performance



## server setup

Log into your AWS account and launch a t2.xlarge EC2 instance, using the latest stable Ubuntu image.

SSH into the instance and run these commands to update the software repository and install the dependencies.

    sudo apt-get update
    sudo apt install -y python3-pip nginx

    sudo nano /etc/nginx/sites-enabled/fastapi_nginx

And put this config into the file (replace the IP address with your EC2 instance's public IP):

    server {
        listen 80;   
        server_name <YOUR_EC2_IP>;
        location / {        
            proxy_pass http://127.0.0.1:8000;    
        }
    }

    sudo service nginx restart
    
 Update EC2 security-group settings for your instance to allow HTTP traffic to port 80.

## launch api

Install dependencies:

    pip install ultralytics fastapi uvicorn

Launch API:

    python3 -m uvicorn main:app
