# coding=utf8
#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText

toList = ["liujiangbei@didichuxing.com"]
host = "smtp.126.com"
user = "liujiangbei"
pwd = "liu!@#631959_"
postFix = "126.com"


def sendMail(toList, sub, content):
  me = "hello"+"<"+user+"@"+postFix+">"
  msg = MIMEText(content, _subtype="html", _charset="gb2312")
  msg["Subject"] = sub
  msg["From"] = me
  msg["To"] = ";".join(toList)

  try:

    s = smtplib.SMTP(host, 25)
    s.connect(host, 25)
    s.login(user, pwd)
    s.sendMail(me, toList, msg.as_string())
    s.close()

    return True
  except Exception, e:

    print str(e)
    return False

if __name__ == '__main__':
  if(sendMail(toList, "Hello", "<div>hello，nice to meet you!</div>")):
    print "send success."
  else:
    print "send failed."

print "done"
