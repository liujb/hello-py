# coding=utf8

import smtplib

from email.mime.text import MIMEText
_user = "578317190@qq.com"
_pwd = "liu!@#631959_"
_to = "liujiangbei@126.com"

# 使用MIMEText构造符合smtp协议的header及body
msg = MIMEText("乔装打扮，不择手段")
msg["Subject"] = "don't panic"
msg["From"] = _user
msg["To"] = _to

try:
  s = smtplib.SMTP("smtp.qq.com", timeout=30)  # 连接smtp邮件服务器,端口默认是25
  s.login(_user, _pwd)  # 登陆服务器
  s.sendmail(_user, _to, msg.as_string())  # 发送邮件
  s.close()
except smtplib.SMTPException, e:
  print str(e)
