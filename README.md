# build-sell-computer-vision-api

## deployment

### backend

#### setup server

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
