# raspberrypi-ipautosend
树莓派或者其他什么linux，使用dhcp时自动发送获取到的ip地址<br>
修改最后一行中的参数<br>
smtp服务器地址、邮箱用户名，邮箱秘密，发件人地址，手贱儿女地址（列表的方式），邮件主题，邮件html内容<br>
sendEmail('smtp.163.com','网易邮箱账号','网易邮箱密码','邮箱邮箱地址',['收件人地址'],'IP Address Of Raspberry Pi',ipaddr)<br>
<br>
<br>
python ip.py测试成功后添加至/etc/rc.local
