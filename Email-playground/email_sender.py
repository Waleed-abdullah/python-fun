import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Waleed Abdullah'
email['to'] = 'anyone@gmail.com'
email['subject'] = 'Well well look what we have here'

email.set_content(html.substitute({'name': 'Waleed'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email', 'password')
    smtp.send_message(email)
    print('sent successfully')
