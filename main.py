import smtplib
import datetime as dt
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open(file="D:\My Programs\Python Programs\Project or Games\Sending E-mail (Using SMTP)\quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes) 
# Email configuration
sender_email = "adityarock704@gmail.com"
receiver_email ="aksh.ntpc@gmail.com"
password =  "cypveyenpqgnhgwh"

# Constructing the email
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = 'Motivational Quote'
body = quote
message.attach(MIMEText(body, 'plain'))

try:
    # Establishing a connection to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        print('Email sent successfully!')
except Exception as e:
    print(f'Error: {e}')