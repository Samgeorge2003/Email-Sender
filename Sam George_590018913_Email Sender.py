import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        # SMTP server setup (Gmail's SMTP server)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        # Create a MIME object
        email = MIMEMultipart()
        email['From'] = sender_email
        email['To'] = recipient_email
        email['Subject'] = subject

        # Attach the message to the email
        email.attach(MIMEText(message, 'plain'))

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, email.as_string())
        server.quit()

        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    # Replace these with your details
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"  # Use an app password if 2FA is enabled
    recipient_email = "recipient_email@gmail.com"
    subject = "Test Email"
    message = "Hello, this is a test email sent using Python!"

    send_email(sender_email, sender_password, recipient_email, subject, message)
