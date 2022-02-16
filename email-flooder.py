import smtplib,os,time
from email.message import EmailMessage

EMAIL_ADDRESS = 'OWN GMAIL'
EMAIL_PASSWORD = 'OWN GMAIL_PASSWORD'

msg = EmailMessage()
msg['Subject'] = 'Hello :D'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'TARGET GMAIL'
msg.set_content('Profile get more')
msg.add_alternative("""\
<!DOCTYPE html>
<html lang="de">
    <head>

    </head>
    <body style="background-color:rgba(0, 0, 0, 0.808)">
        <div style="margin:auto;width:75%;border:4px solid rgba(0, 140, 255, 0.808);padding:10px;border-bottom-left-radius: 30px;">
            <h1 style="text-align: center;font-size:66px;font-family:Arial;color:rgba(204, 207, 218, 0.431);">Sie haben <strong style="color:rgba(255, 255, 255, 0.801);text-decoration:underline;">nichts</strong> gewonnen! :D</h1>
        
        <div style="margin:auto;width:75%;border:0px solid rgba(0, 140, 255, 0.808);padding:10px;border-bottom-left-radius: 30px;">
            <a href="" style="color:whitesmoke;border:3px solid whitesmoke;padding:10px;font-size:33px;font-family:Arial;text-decoration: none;">Rufen Sie uns an</a>
            <a href="" style="color:whitesmoke;border:3px solid whitesmoke;padding:10px;font-size:33px;font-family:Arial;text-decoration: none;">Schreiben Sie eine Mail</a>
        </div>
        </body>
</html>
""", subtype='html')

x = 0
print(" [*] Sending Emails..")
while (x < 100):
    time.sleep(0.4)
    x += 1
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
            smtp.send_message(msg)
            print(" [+] Email has been sent [ %s ]"%(x))
    except Exception as e:
        print(e)
        print(" [ERROR] Could not send Email!")


