import smtplib, ssl, os

sender = 'SENDER'
password = os.getenv("APP_PASS")
receiver = 'RECEIVER'

body_msg = '''Subject: test
I've sent an e-mail with Python'''

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, body_msg)