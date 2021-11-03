import smtplib
from email.message import EmailMessage
from decouple import config

USER_EMAIL = config('USER_EMAIL')
USER_PASS = config('USER_PASS')

contacts = [USER_EMAIL, 'test@example.com']

msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
msg['From'] = USER_EMAIL
msg['To'] = USER_EMAIL

msg.set_content('This is a plain text email')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!<h1/>
    </body>
</html>
""", subtype='html')


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(USER_EMAIL, USER_PASS)

    smtp.send_message(msg)
