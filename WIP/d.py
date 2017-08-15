import pymongo
import json
import ast
import pprint
from scrapy import cmdline
import time
import smtplib

from bson import json_util, ObjectId
from pymongo import MongoClient
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#cmdline.execute("scrapy crawl music".split())
#time.sleep(5)

client = MongoClient()
db = client.viperial

cursor = db.tracks.find({}, {'_id': False})
cursor.limit(20)
cursor.sort([('_id', pymongo.DESCENDING)])
tracklist = []
pl = pprint.PrettyPrinter()

for document in cursor:
	cursor2 = ast.literal_eval(json.dumps(document))
	tracklist.append(cursor2)


listed = pl.pformat(tracklist)
print(listed)


#time.sleep(10)
'''
me = "butler@digitalvassal.com"
you = "jrpearson@me.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Fresh Tracks"
msg['From'] = me
msg['To'] = you

html = """\
<html>
  <head></head>
  <body>
    <p><b>Wa gwarn?</b><br>
	<br>
       Here are some freshly released tracks for your perusal...
	<br>
    </p>
    <p>	
    No need to thank me just doing my job, seriously, do<b> not</b> reply to this message.
    </p>	
   </body>
</html>
"""

emailBody = MIMEText(html, 'html')
emailBody2 = MIMEText(listed, 'plain')
msg.attach(emailBody)
msg.attach(emailBody2)
s = smtplib.SMTP('localhost')
s.sendmail(me, you, msg.as_string())
s.quit()
'''
#pl.pprint(tracklist)
#print ast.literal_eval(json.dumps(test))
