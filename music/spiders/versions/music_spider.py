import scrapy
import urlparse

from music.items import MusicItem

class musicSpider(scrapy.Spider):
    name = "music"
    allowed_domains = ["viperial.cc"]
    start_urls = [
                 "http://www.viperial.cc/tracks/browse/"
                 ]

    def parse(self, response):
        for sel in response.xpath('//ul[@class="cont"]/li'):
		item = MusicItem()
		item ['artist'] = ''.join(sel.xpath('.//b/text()').extract())
		item ['trackName'] = ''.join(sel.xpath('.//strong/text()').extract())
		item ['trackUrl'] = urlparse.urljoin('http://www.viperial.cc',''.join(sel.xpath('a/@href').extract()))
		yield item

	#filename = response.url.split("/")[-2] + '.html'
        #with open (filename, 'wb') as f:
	#     f.write(response.body)
