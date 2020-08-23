from flask import Flask, request, send_file
app = Flask(__name__)
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import socket
import datetime
import pytz
from pyngrok import ngrok
import sys
import os
host=None

@app.route('/',methods=['POST','GET'])
def sendmail():
    if(request.method=='POST'):
        #The mail addresses and password
        sender_address = 'sender@email.post.fix'
        sender_pass = 'pass_of_sender_mail'
        receiver_address = str(request.form['rec_mail'])
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        sub = str(request.form['sub'])   #The subject line
        message['Subject']=sub
        mail_content = str(request.form['content'])
        if(str(request.form['isfiles'])=='Y'):
            files = str(request.form['files']).split('\n')
            n=len(files)
            for i in range(n):
                path = files[i]
                try:
                    attachment = open(path, "rb") 
                except:
                    continue
                # instance of MIMEBase and named as p 
                p = MIMEBase('application', 'octet-stream') 
                # To change the payload into encoded form 
                p.set_payload((attachment).read()) 
                # encode into base64 
                encoders.encode_base64(p)
                words=None
                if (platform.system()=='Windows'):
                    words=path.split('\\')
                else:
                    words=path.split('/')
                p.add_header('Content-Disposition', "attachment; filename= %s" %words[-1]) 
                # attach the instance 'p' to instance 'msg' 
                message.attach(p)
        #The body and the attachments for the mail
        url="{0}/check/{1}/{2}/sending.jpg".format(host,receiver_address,sub)
        message.attach(MIMEText('<b>{0}</b><br/><img src={1} alt=" "></img>'.format(mail_content,url), 'html'))
        #Create SMTP session for sending the mail
        try:
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
        except:
            return 'Error in connecting smtp'
        try:
            session.login(sender_address, sender_pass) #login with mail_id and password
            text = message.as_string()
        except:
            return 'Error in login'
        try:
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            print(text)
            return 'Mail Sent'
        except:
            print('Err in sending')
            return "Mail not sent"
    if(request.method=='GET'):
        return "<form action=\"/\" method=\"POST\">\n"+"<input id=\"rec_mail\" name=\"rec_mail\" type=\"text\" placeholder=\"Receiver's mail add\"/><br/><input id=\"sub\" name=\"sub\" type=\"text\" placeholder=\"Subject\"/><br/>"+"<textarea id=\"content\" name=\"content\" placeholder=\"Body of Mail\"></textarea><br/>"+"<input type=\"radio\" id=\"isfiles\" name=\"isfiles\" value=\"Y\">Y</input><br/>"+"<input type=\"radio\" id=\"isfiles\" name=\"isfiles\" value=\"N\">N</input><br/>"+"<textarea id=\"files\" name=\"files\" placeholder=\"Enter path of files with extention and each should be in different line\"></textarea><br/>"+"<input type=\"submit\" value=\"Send mail\"/></form>"
@app.route('/check/<mail>/<sub>/<filename>')
def check(mail,sub,filename):
    try:
        file=open("./email_log.txt",'a+')
        file.write("mail for {0} with subject {1} has opened at {2}\n".format(mail,sub,datetime.datetime.now(pytz.timezone('Asia/Kolkata'))))
        file.close()
        return send_file(filename, mimetype="image/jpg")
    except IOError:
        print("Error opening email_log.txt")
        return send_file(filename, mimetype="image/jpg")

host=sys.argv[1]
app.run('127.0.0.1',port=5000,debug=True)
