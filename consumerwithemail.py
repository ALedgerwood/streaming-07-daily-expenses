
import pika
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv  # Import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Function to send email alerts
def send_email_alert(subject, message):
    # Retrieve email credentials from environment variables
    sender_email = os.getenv("FROM_EMAIL")
    sender_password = os.getenv("PASSWORD")
    recipient_email = 'teaginny@gmail.com'

    # Print the values for debugging
    print(f"FROM_EMAIL: {sender_email}")
    print(f"PASSWORD: {sender_password}")

    # Create a MIMEText object with the message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to the SMTP server (for Gmail, use 'smtp.gmail.com')
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)

        # Send the email
        smtp_server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email alert sent successfully.")
    except Exception as e:
        print(f"Error sending email alert: {str(e)}")
    finally:
        # Close the SMTP server connection
        smtp_server.quit()

# Callback function to process messages
def callback(ch, method, properties, body):
    message = body.decode()
    print(f"Received alert: {message}")

    # Send email alert with the message
    send_email_alert("Expense Alert", message)

    # Introduce a sleep time (e.g., 1 second) between message processing
    time.sleep(1)

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='expense_alerts')

# Set up the callback function
channel.basic_consume(queue='expense_alerts', on_message_callback=callback, auto_ack=True)

# Start consuming messages
print('Waiting for expense alerts. To exit, press CTRL+C')
channel.start_consuming()

