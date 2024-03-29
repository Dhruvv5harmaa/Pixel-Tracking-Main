import json
import boto3

def lambda_handler(event, context):
    client = boto3.client("ses")
    subject = "Test subject from Lambda"

    receiver_id = 7

    # HTML content for the email body with embedded tracking pixel
    body = f"""
    <html>
    <body>
        <p>Email Content.</p>
        <!-- Tracking pixel (invisible image) with onclick attribute -->
        <img src ="http://35.154.178.91:8000/about?id={receiver_id}" height=1 width=1>
        <a href="http://35.154.178.91:8000/about?id={receiver_id}">Click here</a> to visit the about page.
    </body>
    </html>
    """

    message = {
        "Subject": {"Data": subject},
        "Body": {"Html": {"Data": body}}
    }

    response = client.send_email(
        Source="dhruvsharmaindore@gmail.com",
        Destination={"ToAddresses": ["gs2017085@sgsitsindore.in"]},
        Message=message
    )

    return response






    
    
    
    
    
    
    