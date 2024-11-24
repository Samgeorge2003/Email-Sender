# Email-Sender
A Python script to send emails using the smtplib library. The script uses a Gmail SMTP server but can be adjusted for other email providers.
# Key Points:
* SMTP Server:
Gmail: smtp.gmail.com on port 587
Outlook: smtp.office365.com on port 587
Yahoo: smtp.mail.yahoo.com on port 465 (SSL)
Adjust the server and port for other providers.
* Secure Login:
If you’re using Gmail, enable "Less secure app access" in your account settings. Alternatively, generate an App Password for added security (recommended if 2FA is enabled).
* Dependencies:
This script uses Python’s built-in libraries, so no additional installations are required.
* Error Handling:
The script includes basic exception handling to provide feedback if the email fails to send.
* Privacy:
Avoid hardcoding sensitive information like passwords. Use environment variables or configuration files instead.
