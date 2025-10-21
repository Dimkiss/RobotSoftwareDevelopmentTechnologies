# import os
# import smtplib
# from dotenv import load_dotenv, find_dotenv
# from faker import Faker
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders

# env_path = find_dotenv(filename=".env", usecwd=True)
# load_dotenv(env_path)

# EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
# EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
# SENDER_FILTER = os.getenv("SENDER_FILTER")

# SMTP_SERVER = "smtp.gmail.com"
# SMTP_PORT = 587

# fake = Faker("ru_RU")
# full_name = fake.name()
# company = fake.company()
# subject = f"Отчёт по проекту {company}"
# body = f"""
# <html>
#   <body>
#     <h2>Здравствуйте!</h2>
#     <p>тестовое письмо от <b>{full_name}</b> ({company}).</p>
#   </body>
# </html>
# """

# filename = "report.pdf"

# msg = MIMEMultipart()
# msg["From"] = EMAIL_ADDRESS
# msg["To"] = SENDER_FILTER
# msg["Subject"] = subject
# msg.attach(MIMEText(body, "html"))

# with open(filename, "rb") as f:
#     part = MIMEBase("application", "octet-stream")
#     part.set_payload(f.read())
# encoders.encode_base64(part)
# part.add_header("Content-Disposition", f"attachment; filename={os.path.basename(filename)}")
# msg.attach(part)

# with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
#     smtp.starttls()
#     smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#     smtp.send_message(msg)
import os
import imaplib
from dotenv import load_dotenv, find_dotenv

env_path = find_dotenv(filename=".env", usecwd=True)
load_dotenv(env_path)

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SENDER_FILTER = os.getenv("SENDER_FILTER")

IMAP_SERVER = "imap.gmail.com"

mail = imaplib.IMAP4_SSL(IMAP_SERVER)
mail.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
mail.select("inbox")

status, data = mail.search(None, f'(FROM "{SENDER_FILTER}")')

if status == "OK":
    email_ids = data[0].split()
    print(f"Найдено писем от {SENDER_FILTER}: {len(email_ids)}")
    for eid in email_ids:
        mail.store(eid, '+FLAGS', '\\Seen')
    print("Все найденные письма помечены как прочитанные")
else:
    print("Ошибка при поиске писем.")

mail.logout()
