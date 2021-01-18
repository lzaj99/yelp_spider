# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PlaceInfoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fetched_time = scrapy.Field()
    name = scrapy.Field()
    rating = scrapy.Field()
    num_of_reviews = scrapy.Field()
    address = scrapy.Field()
    district = scrapy.Field()
    contact_info = scrapy.Field()
    description = scrapy.Field()
    detail = scrapy.Field()
