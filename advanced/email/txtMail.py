#!/usr/bin/python
# coding=utf8
# smtp==simple mail transfer protocol

import smtplib
import email.encoders

sender = "liujiangbei@126.com"
receivers = ["578317190@qq.com"]

host = "smtp.126.com"
user = "liujiangbei@126.com"
pwd = "liu!@#631959_"

# print email.encoders.encode_base64("sdfsfsf")

message = 'hello world'

try:

  s = smtplib.SMTP(host, port=25, timeout=30)
  # s.set_debuglevel(1)
  # s.ehlo("578317190")

  s.esmtp_features["auth"] = "LOGIN PLAIN"  # "LOGIN PLAIN"
  s.login(user, pwd)

  # s.docmd("AUTH", "%s %s" % ("LOGIN",  email.encoders.encode_base64(user)))
  # s.docmd(email.encoders.encode_base64(pwd))

  s.sendmail(sender, receivers, message)
  s.close()
  print "sucessfully sent email."

except smtplib.SMTPException, e:
  print str(e)
  print "Error: unable to send email"
