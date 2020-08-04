from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from myid import ID, PW

SMTP_SERVER = 'smtp.naver.com'
SMTP_PORT = 465
SMTP_USER = ID
SMTP_PASSWORD = PW

def send_email(name, addr, content, attachment=None):
    msg = MIMEMultipart('alternative')
    
    if attachment:
        msg = MIMEMultipart('mixed')
    

    msg['From'] = SMTP_USER + '@naver.com'
    msg['To'] = addr
    msg['Subject'] = name + '님에게 메일 도착'


    text = MIMEText(content, _charset='utf-8')
    msg.attach(text)

    if attachment:
        import os
        from email.mime.base import MIMEBase
        from emila import encoders

        fileobject = MIMEBase('application', 'octect-stream')
        file_data.set_payload(open(attachment, 'rb').read() )
        encoders.encode_base64(file_data)

        filename = os.path.basename(attachment)
        file_data.add_haeder('Content-Disposition','attachment; filename="' + filename +'"')
        msg.attach(file_data)


    smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
    smtp.login(SMTP_USER, SMTP_PASSWORD)
    smtp.sendmail(SMTP_USER + '@naver.com', addr, msg.as_string())
    smtp.close()

send_email('손재현', 'alghost.sjh9391985@naver.com', '내용','result.csv')