#/bin/env python
# -*-coding:utf8-*-
import socket
import fcntl
import time
import struct
import smtplib
import urllib
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

#发送邮件的基本函数，参数依次如下
# smtp服务器地址、邮箱用户名，邮箱密码，发件人地址，收件人地址（列表的方式），邮件主题，邮件html内容
def sendEmail(smtpserver,username,password,sender,receiver,subject,msghtml):
    msgRoot = MIMEMultipart('related')
    msgRoot["To"] = ','.join(receiver)
    msgRoot["From"] = sender
    msgRoot['Subject'] =  subject
    msgText = MIMEText(msghtml,'html','utf-8')
    msgRoot.attach(msgText)
    #sendEmail
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()

# 检查网络连同性
def check_network():
    while True:
        try:
            result=urllib.urlopen('http://baidu.com').read()
            print result
            print "Network is Ready!"
            break
        except Exception , e:
           print e
           print "Network is not ready,Sleep 5s...."
           time.sleep(5)
    return True

# 获得本机接口的ip地址
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("1.1.1.1",80))
    ipaddr=s.getsockname()[0]
    s.close()
    return ipaddr

#利用ip138.com获取外网ip
def get_iip_address():
    url = r'http://2017.ip138.com/ic.asp'
    r = requests.get(url)
    txt = r.text
    iipaddr = txt[txt.find("[") + 1: txt.find("]")]
    #print('ip:' + ip)
    return iipaddr

#执行过程
if __name__ == '__main__':
    check_network()
    ipaddr=get_ip_address()
    iipaddr=get_iip_address()
	#封装邮件内容
    mail=('internal ip:'+ ipaddr+'<br>'+'internet ip:' + iipaddr)
    sendEmail('smtp.163.com','网易邮箱账号','网易邮箱密码','邮箱邮箱地址',['收件人地址'],'IP Address Of Raspberry Pi',mail)
