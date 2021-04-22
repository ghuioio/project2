# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TgddtutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
    ram = scrapy.Field()
    memory = scrapy.Field()
    battery = scrapy.Field()
    star = scrapy.Field()
    pass
