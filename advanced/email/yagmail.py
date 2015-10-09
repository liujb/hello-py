# coding=utf8
#!/usr/bin/python

import yagmail

yag = Connect('liujiangbei88@gmail.com',
                      'jiangbei6631959@', "smtp.gmail.com", 25, set_debuglevel=1)
yag.send(["liujiangbei@126.com"], Subject='Hello', Body="Hello")



