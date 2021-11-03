import smtplib
from decouple import config

USER_EMAIL = config('USER_EMAIL')
USER_PASS = config('USER_PASS')

# using gmail
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(USER_EMAIL, USER_PASS)

    subject = 'Grab dinner this weekend?'
    body = 'How about dinner at 6pm this Saturday?'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(USER_EMAIL, USER_EMAIL, msg)
 

# using localhost
# with smtplib.SMTP('localhost', 1025) as smtp:

#     subject = 'Grab dinner this weekend?'
#     body = 'How about dinner at 6pm this Saturday?'

#     msg = f'Subject: {subject}\n\n{body}'

#     smtp.sendmail(USER_EMAIL, USER_PASS, msg)
    