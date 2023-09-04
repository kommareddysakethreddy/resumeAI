

from jinja2 import Template
import smtplib
from email.message import EmailMessage
# from generate_resume import generate_resume
import pdfcrowd
import sys

def generate_resume(json_data, template_file_path=r"utils\templates\resume_template.html"):
    # print(0)
    with open(template_file_path, 'r') as template_file:
        template_content = template_file.read()
    # print(1)
    template = Template(template_content)
    # print(2)
    rendered_html = template.render(**json_data)
    # print(3)
    # write to example.html
    with open('example.html', 'w') as f:
        f.write(rendered_html)
    # print(4)
    return rendered_html

def generate_pdf(html):
    try:
        # create the API client instance
        client = pdfcrowd.HtmlToPdfClient('<PDFCROWD_USERNAME>', '<PDFCROWD_API_KEY>')

        # run the conversion and write the result to a file
        client.convertFileToFile(html, 'resume.pdf')
    except pdfcrowd.Error as why:
        # report the error to the standard error stream
        sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))

        # rethrow or handle the exception
        raise

def mail(email, json):
    # print(0)
    body=generate_resume(json)
    # print(0.5)
    generate_pdf('./example.html')
    EMAIL_ADDRESS = <EMAIL_ADDRESS>
    EMAIL_PASSWORD = <EMAIL_PASSWORD>
    # print(1)
    contacts = []
    contacts.append(email)
    msg = EmailMessage()
    msg['Subject'] = 'Auto-generated Resume (See attachments)'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = contacts
    # print(2)
    # attach file to mail
    files = ['resume.pdf']
    for file in files:
        with open(file, 'rb') as f:
            file_data = f.read()
            file_name = f.name
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

    # msg.set_content('Please Find the attachments')

    # msg.add_alternative(body, subtype='html')
    # print(3)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
    print("Email sent successfully")


