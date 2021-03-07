import smtplib
from random import randint
from email.utils import COMMASPACE, formatdate
from email.mime.text import MIMEText

text_subtype = 'plain'
otp=str(randint(0,100000))
def main(em):
    content="""\
    Please don't disclose your otp to any one , bank never ask for such private credentials.
    your otp is :""" + otp

    subject="ATM OTP"
    sender="isjamrezaul08@gmail.com"


    msg = MIMEText(content, text_subtype)
    msg['Subject']=       subject
    msg['From']   = sender
    msg['Date'] = formatdate(localtime=True)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("isjamrezaul08@gmail.com", "Riju29feb@")
    server.sendmail(sender, em, msg.as_string())

