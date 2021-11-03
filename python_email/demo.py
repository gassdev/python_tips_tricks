import smtplib
from email.message import EmailMessage
import imghdr
from decouple import config

USER_EMAIL = config('USER_EMAIL')
USER_PASS = config('USER_PASS')

msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = USER_EMAIL
msg['To'] = USER_EMAIL
msg.set_content('Image attached...')

files = ['img.png', 'photo.png']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(USER_EMAIL, USER_PASS)

    smtp.send_message(msg)
