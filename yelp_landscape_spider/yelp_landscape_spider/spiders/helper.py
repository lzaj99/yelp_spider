from __future__ import unicode_literals

import os
import codecs
import copy
import yaml

#xpath example

# name xpath
#/html/body/yelp-react-root/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/ul/li[3]/div/div/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div/h4/span/a/text()
#rating
#/html/body/yelp-react-root/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/ul/li[3]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div[1]/span/div/@aria-abel
#num of reviews
#/html/body/yelp-react-root/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/ul/li[3]/div/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div[2]/span/text()
#address
#/html/body/yelp-react-root/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/ul/li[3]/div/div/div/div[2]/div[1]/div/div[2]/div/address/div/div/div/p/span/text()
#district
#/html/body/yelp-react-root/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/ul/li[4]/div/div/div/div[2]/div[1]/div/div[2]/div/div/div/div/div/p/text()
#phone
#/html/body/yelp-react-root/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/ul/li[3]/div/div/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div/p/text()
#description
#/html/body/yelp-react-root/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/ul/li[3]/div/div/div/div[2]/div[1]/div/div[1]/div/div[3]/div/div/span/span/span/a/text()
#detail
#/html/body/yelp-react-root/div[1]/div[3]/div/div[1]/div[1]/div[2]/div/ul/li[3]/div/div/div/div[2]/div[2]/div/div/div/div/p/text()





class SpiderHelper:
    _conf_path = os.path.join(os.path.dirname(__file__), 'api.yaml')
    with codecs.open(_conf_path, mode = 'r') as conf_file:
        conf = yaml.load(conf_file)

    @staticmethod
    def get_search_list_info():
        search_list_info = copy.deepcopy(SpiderHelper.conf['search_list_info'])

        #print(search_list_urls_base)
        return search_list_info
    @staticmethod
    def get_xpath():
        xpath_info = copy.deepcopy(SpiderHelper.conf['xpath_info'])
        return xpath_info



if __name__ == '__main__':
    # print os.path.dirname(__file__)

    print(SpiderHelper.get_xpath())
