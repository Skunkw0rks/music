# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MusicItem(scrapy.Item):
    artist = scrapy.Field()
    trackName = scrapy.Field()
    trackUrl = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
