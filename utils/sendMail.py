
import os
import smtplib
import imghdr
from email.message import EmailMessage


def mail(email, body):

    EMAIL_ADDRESS = <EMAIL>
    EMAIL_PASSWORD = <APP_PASSWORD>

    contacts = []
    contacts.append(email)
    msg = EmailMessage()
    msg['Subject'] = ''
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = contacts

    msg.set_content('Please Find the attachments')

    msg.add_alternative(body, subtype='html')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
