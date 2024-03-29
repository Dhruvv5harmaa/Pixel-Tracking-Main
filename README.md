# Pixel-Tracking-Main


Steps to Deploy Flask on EC2 and activating the link.
1. Deploy Flask code on EC2 AWS.
2. change directory to "cd Pixel-Tracking-Main"
3. Make virtual env
4. "source venv/bin/activate" to activate env
5. now run the Gunicorn server "gunicorn -b 0.0.0.0:8000 app:app "


Steps to send Email.<br>
1.Make Lambda function and copy the code.<br>  
2.Copy the public link of EC2 instance and paste in img tag and the href link.<br>
3.Then click on send to send the email using AWS Lambda and AWS SES. <br>
4.Track of reciever's data is shown on EC2 logs and stored in images/spy_pixel_logs.txt <br>
