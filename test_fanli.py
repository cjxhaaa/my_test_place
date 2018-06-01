import requests
from lxml import etree
import json
import re
import csv
import os


SESSION = requests.session()

Header = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Host':'www.rebatesme.com',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}


def request(method, url, **kwargs):
	kwargs.setdefault('timeout', 90)
	kwargs.setdefault('headers', Header)
	r = SESSION.request(method, url, **kwargs)
	r.xpath = etree.HTML(r.text).xpath
	return r


class FanLi():
    def __init__(self):
        self.csv_name = 'rebatesme.csv'
        self.response = request('GET','http://www.rebatesme.com/mycenter/myorders/')
        self.next_url = ''
        self.all_lists = []
        self.headers = []
        
    def get_all(self):
        while True:
            self.get_one_page()
            if self.has_next_page():
                self.get_next_page()
            else:
                break
        with open(self.csv_name, 'w') as c:
            c_csv = csv.DictWriter(c, self.headers)
            c_csv.writeheader()
            c_csv.writerows(self.all_lists)
    
    def get_one_page(self):
        columns = self.response.xpath('//div[@class="order_ul_list"]/ul')
        if not self.next_url:
            page_headers = columns[0].xpath('./li/text()')
            for head in page_headers[:6]:
                self.headers.append(head.strip())
        out_lists = []
        for column in columns[1:]:
            contents = column.xpath('./li/text()')[:6]
            inner_list = []
            for content in contents:
                inner_list.append(content.strip())
            inner_dict = dict(zip(self.headers,inner_list))
            out_lists.append(inner_dict)
        self.all_lists.extend(out_lists)
            
    def has_next_page(self):
        self.next_url_place = self.response.xpath('//div[@id="order_foot"]//a[@class="next"]/@href')
        if self.next_url_place:
            self.next_url = self.next_url_place[0]
            return True
        return False
        
    def get_next_page(self):
        self.response = request('GET',self.next_url)
        
if __name__ == "__main__":
    m = FanLi()
    m.get_all()

