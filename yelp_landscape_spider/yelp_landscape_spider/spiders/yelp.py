import logging
from scrapy.spiders import Spider
from scrapy.http import TextResponse, Request
from yelp_landscape_spider.items import PlaceInfoItem
import time
import yaml
import json

from .helper import SpiderHelper



class PlaceListSpider(Spider):
    #Spider task
    # The name of the spider. This attribute is required by the Scrapy
    name = 'yelp'

    # The domain that spider to crawl
    allowed_domains = ['yelp.com']

    def __init__(self, find = 'landmarks and historical buildings', area = 'New York', page_num = 7, **kwargs):
        super(PlaceListSpider, self).__init__(**kwargs)
        #when pass the parameter, only character and digit accrpted in url
        self.find = find
        self.area = area
        # here the ' ' in search keywords need to be transformed to '%20'
        self.modify_keywords()
        self.page_num = page_num
        self.spider_helper = SpiderHelper()


    def start_requests(self):

        if self.argument_valid():
            for i in range(self.page_num):
                request_info = self.spider_helper.get_search_list_info()
                request_info['url'] = request_info['url'].format(target = self.find, area = self.area, page_num = str(i))
                #print(request_info)
                yield Request(**request_info)
        else:
            pass

    def parse(self, response: TextResponse):
        if response.status == 200:
            xpath_info = self.spider_helper.get_xpath()

            for i in range(3, 13):
                xpath_item = {}
                item = PlaceInfoItem()
                xpath_item['name'] = xpath_info['base'].format(item_num = str(i)) + xpath_info['name']
                xpath_item['rating'] = xpath_info['base'].format(item_num = str(i)) + xpath_info['rating']
                xpath_item['num_of_reviews'] = xpath_info['base'].format(item_num = str(i)) + xpath_info['num_of_reviews']
                xpath_item['address'] = xpath_info['base'].format(item_num = str(i)) + xpath_info['address']
                xpath_item['district'] = xpath_info['base'].format(item_num = str(i)) + xpath_info['district']
                xpath_item['contact_info'] = xpath_info['base'].format(item_num = str(i)) + xpath_info['contact_info']
                xpath_item['description'] = xpath_info['base'].format(item_num = str(i)) + xpath_info['description']
                xpath_item['detail'] = xpath_info['base'].format(item_num = str(i)) + xpath_info['detail']
                item['fetched_time'] = int(time.time())
                item['name'] = self.handle_info(response.xpath(xpath_item['name']).extract())
                item['rating'] = self.handle_info(response.xpath(xpath_item['rating']).extract())
                item['num_of_reviews'] = self.handle_info(response.xpath(xpath_item['num_of_reviews']).extract())
                item['address'] = self.handle_info(response.xpath(xpath_item['address']).extract())
                item['district'] = self.handle_info(response.xpath(xpath_item['district']).extract())
                item['contact_info'] = self.handle_info(response.xpath(xpath_item['contact_info']).extract())
                item['description'] = self.handle_info(response.xpath(xpath_item['description']).extract())
                item['detail'] = self.handle_info(response.xpath(xpath_item['detail']).extract())
                yield item

            #print(xpath_info)

        else:
            #log.msg('Crawling failed: {}'.format(response.url))
            pass



    def handle_info(self, sorce_info):
        if not sorce_info:
            return ''
        else:
            return sorce_info[0]



    def modify_keywords(self):
        self.find = self.find.replace(' ', '%20')
        self.area = self.area.replace(' ', '%20')

    def argument_valid(self):
        return self.find and self.area
