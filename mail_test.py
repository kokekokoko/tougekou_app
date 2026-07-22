import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg['From'] = 'kenji12.973@gmail.com'
msg['To'] = 'a22.emtw@g.chuo-u-ac.jp'
msg['Subject'] = 'Test mail'
body = "this is a test mail"
msg.attach(MIMEText(body, 'plain'))

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = 'kenji12.973@gmail.com'
smtp_password = 'Kenji18427365'  # アプリパスワードを入力してください

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_user, smtp_password)
    text = msg.as_string()
    server.sendmail(msg['From'], msg['To'], text)
    server.quit()
    print("メールが送信されました")
except Exception as e:
    print("エラーが発生しました", e)