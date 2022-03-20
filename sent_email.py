from email.mime.text import MIMEText
import smtplib


def send_email(email, height):
    from_email = "ank15121996@gmail.com"
    from_pass  ="*********"
    to_email   = email

    subject = "Height Data"
    message = "Hey there, your height is <strong>%s</strong>. " %height
    msg= MIMEText(message,"html")
    msg['subject']=subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_pass)
    gmail.send_message(msg)

    print(email,height)