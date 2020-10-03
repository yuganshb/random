import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

from_mail = "<email_here>"
to_mail =[""]
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login("<email>", "<password>")
html = """\
            <html>
              <head></head>
              <body>
                <p>Hi!<br>
                   Email content</a>.
                </p>
              </body>
            </html>
            """ 
x = MIMEText(html,'html')
msg = MIMEMultipart()
msg["Subject"] = ""
msg["From"] = from_mail
msg["To"] = ",".join(to_mail)
msg.attach(x)
server.sendmail(from_mail, [""],msg.as_string())
server.quit()
