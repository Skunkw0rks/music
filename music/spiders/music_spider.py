import scrapy
import urlparse

from music.items import MusicItem

class musicSpider(scrapy.Spider):
    name = "music"
    allowed_domains = ["viperial.com"]
    start_urls = [
                 "http://www.viperial.com"
    ]

    def parse(self, response):
        for sel in response.xpath('//section[@class="latest-tracks"]/ul[@class="latest-tracks tracks-list clearfix"]/li'):#<-REMEMBER IT MUST BE A LI
                item = MusicItem()
                item ['artist'] = sel.xpath('.//span[@class="artist"]/text()').extract()#<-THE .// MEANS SEARCH WITHIN THE LOOP
                item ['trackName'] = sel.xpath('.//span[@class="name"]/text()').extract()
                item ['trackUrl'] = sel.xpath('.//@href').extract()
                yield item
