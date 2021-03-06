#!/usr/bin/env python

import pymongo
import json
import pprint
import smtplib
import ast

from pymongo import MongoClient
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

client = MongoClient()
db = client.viperial
tracklist = []
pl = pprint.PrettyPrinter()

cursor = db.tracks.find({}, {'_id': False})
cursor.limit(20)
cursor.sort([('_id', pymongo.DESCENDING)])

for document in cursor:
	cursor2 = ast.literal_eval(json.dumps(document))
	tracklist.append(cursor2)

listed = pl.pformat(tracklist)

me = "butler@digitalvassal.com"
you = "jrpearson@me.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Special Delivery"
msg['From'] = me
msg['To'] = you

emailBody = MIMEText(listed.encode('utf-8'),'plain','utf-8')
msg.attach(emailBody)
s = smtplib.SMTP('localhost')
s.sendmail(me, you, msg.as_string())
s.quit()

