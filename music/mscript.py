from pymongo import MongoClient
from scrapy import cmdline
cmdline.execute("scrapy crawl music".split())

client = MongoClient()
db = client.viperial

joints = "db.tracks.find().sort({_id::1}).limit(20).pretty().shellPrint();" 

for document in joints:
	print (document) 
