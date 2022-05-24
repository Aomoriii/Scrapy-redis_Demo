# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SuningbookItem(scrapy.Item):
    L1_cate = scrapy.Field()
    L2_href = scrapy.Field()
    L2_name = scrapy.Field()
