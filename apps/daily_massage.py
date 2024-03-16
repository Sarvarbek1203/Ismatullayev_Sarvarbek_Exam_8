import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
from root.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from django.contrib.auth.models import User


sender_email = EMAIL_HOST_USER
sender_password = EMAIL_HOST_PASSWORD
receiver_email = User.objects.get('email').email


subject = "Yangi mahsulotlar qo'shildi!"
message = """
Assalomu alaykum,

Bugun soat 8:00 da bizda yangi mahsulotlar qo'shildi. Iltimos, bizning saytimizga kiring va yangi mahsulotlarni ko'ring!

Yuqorida qo'shilgan mahsulotlar haqida batafsil ma'lumotlarni olish uchun quyidagi havolaga o'ting: [Mahsulotlar sahifasi havolasi]

Hurmat bilan,
Sizning kompaniyangiz
"""


msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject


msg.attach(MIMEText(message, 'plain'))


try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()
    print("Xabar muvaffaqiyatli yuborildi!")
except Exception as e:
    print("Xabar yuborishda xatolik:", e)

