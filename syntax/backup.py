'''
module docstring
'''

import os
import time

source = [r'C:\/inetpub', r'C:\/PerfLogs']
targetDir = r'C:\/backup'
target = targetDir + time.strftime('%Y%m%d%H%M%S')+'.zip'
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

print zip_command
if os.system(zip_command) == 0:
  print 'Successful backup to', target
else:
  print 'Backup failed'
