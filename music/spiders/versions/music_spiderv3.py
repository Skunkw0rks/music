import scrapy
import urlparse

from music.items import MusicItem

class musicSpider(scrapy.Spider):
    name = "music"
    allowed_domains = ["viperial.info"]
    start_urls = [
                 "http://www.viperial.info"
                 ]

    def parse(self, response):
        for sel in response.xpath('//section[@class="latest-tracks"]'):
                item = MusicItem()
                item ['artist'] = ''.join(sel.xpath('.//span[@class="artist"]/text()').extract())
                item ['trackName'] = ''.join(sel.xpath('.//span[@class="name"]/text()').extract())
                item ['trackUrl'] = urlparse.urljoin('http://www.viperial.info',''.join(sel.xpath('.//ul[@class="latest-tracks tracks-list clearfix"]//@href').extract()))
                yield item
