import requests,ipdb,json
from lxml import etree



def get_response(url):
    response = requests.get(url)
    # with open('/tmp/t.html','r') as f:
    #     response = f.read()
    # t = etree.HTML(text=response)
    response.xpath = etree.HTML(text=response.text).xpath
    return response

def find_all_category(response):
    all_category = {}
    for level in response.xpath('//nav[@id="navigation"]//ul[@class="menu-category level-1"]/li'):
        level1_text = level.xpath('./a[@class="has-sub-menu"]/text()')[0].strip('\n')
        all_category.setdefault(level1_text, [])
        for ul in level.xpath('./div[@class="level-2"]/ul[@class="menu-vertical"]'):
            level2_text = ul.xpath('./li/a/text()')[0].strip('\n')
            all_category[level1_text].append(level2_text)
    return all_category

def find_all_category(response):
    all_category = {}
    # i1 = 1
    for level in response.xpath('//nav[@id="navigation"]//ul[@class="menu-category level-1"]/li'):
        # print('level1-',i1)
        level1_text = level.xpath('./a[@class="has-sub-menu"]/text()')[0].strip('\n')
        all_category.setdefault(level1_text,[])
        # i1 += 1
        # i2 = 1
        for ul in level.xpath('./div[@class="level-2"]/ul[@class="menu-vertical"]'):
            # print('level2-', i2)
            level2_text = ul.xpath('./li/a/text()')[0].strip('\n')
            all_category[level1_text].append(level2_text)

    return all_category

if __name__ == '__main__':
    url = 'http://www.gnc.com/255215.html'
    rr = get_response(url)
    category = find_all_category(rr)
    uu = 'cleansing-detox'
    for c in category.keys():
        if uu.replace('-',' ') == c.replace('& ','').lower():
            print('ok 1')
        for x in category[c]:
            if uu.replace('-',' ') == x.replace('& ','').lower():
                print(uu)
                print(x)
                print('ok 2')
