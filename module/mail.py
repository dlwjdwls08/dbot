import smtplib
from email.mime.text import MIMEText

s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('ljj20080520@gmail.com',)