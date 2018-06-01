import requests,ipdb
from lxml import etree
import json
import re

SESSION = requests.session()


Header1 = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate, br',
	'Accept-Language':'zh-CN,zh;q=0.9,zh-TW;q=0.8,ja;q=0.7',
	'Host':'www.shopspring.com',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
# cookies = {
# 	"Cookie": "shippingCountry=US; "
# 			  "currency=USD; "
# }
Headers = {
		# 'Accept':'application/json, text/javascript, */*;',
		# 'Accept-Encoding':'gzip, deflate, br',
		# 'Accept-Language':'zh-CN,zh;q=0.9,zh-TW;q=0.8,ja;q=0.7',
		# 'Content-Length':'57',
		# 'Content-Type':'application/x-www-form-urlencoded',
		# 'Host':'www.shopspring.com',
		# 'Referer':'https://www.shopspring.com/signin',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    	'Accept-Encoding': 'gzip, deflate, sdch',
    	'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
		"Upgrade-Insecure-Requests":"1"
		# 'X-CSRF-Token':'aojqBoD0fOeT2VfhrHT5exI2KXndaJUz8Em37CkNYxWCqmJYNOkapl11A6xcUon63KYAwH5vFtt7bnTC2r3SxQ==',
		# "Accept":"*/*",
        # "Accept-Encoding":"gzip, deflate, br",
        # "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        # "Connection":"keep-alive",
        # 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
		# 'Cookie':'miid=530033290273529942; '
		# 		 'cna=v7p9EuzMdSMCATplzXQzF0vc; '
		# 		 'hng=CN%7Czh-CN%7CCNY%7C156; '
		# 		 'thw=cn; '
		# 		 'UM_distinctid=1600fe7afb369b-05f0be014a8f7f-173b6d56-fa000-1600fe7afb45e1; '
		# 		 't=382f08be2da534c1388a12bd96396c8b; '
		# 		 'v=0; '
		# 		 'cookie2=2e29bc99d8debb9764831d4e6c6a8af0; '
		# 		 '_tb_token_=eeefe959d6eb3; '
		# 		 'alitrackid=www.taobao.com; '
		# 		 'uc3=sg2=W5pXzVeIEIRlt4yFm5ofXdc1cAzOsA2dOGC%2F6oqS%2FJw%3D&nk2=AHDZa0dbPw%3D%3D&id2=VAYpzJP5ro03&vt3=F8dBzLeFvOcyMyJNMEI%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D; '
		# 		 'existShop=MTUxNTIxOTc1OA%3D%3D; '
		# 		 'uss=UITtlrNlMQK4w%2Fi3yxtbAI%2B1aHgzhbGufnDcvhRci5mmwGgg%2BUQz1c8AiSg%3D; '
		# 		 'lgc=cjxh789; '
		# 		 'tracknick=cjxh789; '
		# 		 'sg=91a; '
		# 		 'cookie1=B0b0bbkVv5p%2FLf7ekRxH4AhjUubdb%2B8RGzzXTBj0%2BBk%3D; '
		# 		 'unb=771458091; '
		# 		 'skt=b2c3ded9ed331eb3; '
		# 		 '_cc_=Vq8l%2BKCLiw%3D%3D; '
		# 		 'tg=0; '
		# 		 '_l_g_=Ug%3D%3D; '
		# 		 '_nk_=cjxh789; '
		# 		 'cookie17=VAYpzJP5ro03; '
		# 		 'enc=6dkTRAsQVd5XUGyLPB5caa%2BU8VAWiArYDPVtATDah8mghjIky8UZMAXE%2Fw58BHUIDWYxTNWEMNNJrA4NEEBVwQ%3D%3D; '
		# 		 'lastalitrackid=login.taobao.com; '
		# 		 'mt=ci=0_1; '
		# 		 'uc1=cookie14=UoTdfklFUhfBlA%3D%3D&lng=zh_CN&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&existShop=false&cookie21=UtASsssmeWzt&tag=8&cookie15=UtASsssmOIJ0bQ%3D%3D&pas=0; '
		# 		 'JSESSIONID=E3A1A7E373007E936815B99754273458; isg=Ap-foqK4OQaWFD6zW7Uo9EfdLvXprPPO5msASjHsO86VwL9COdSD9h2S9mZF'
		# 'Cookie':'_uuid=0B479BC1-2CA6-4AA0-B099-8FFAB4A3FB38; '
		# 		 'SERVER_ID=17c3dc44-bcc32c93; '
		# 		 'Hm_lvt_a3a5d79d073a1c3f23a74df6bc6a6c2c=1514427078; '
		# 		 'scarab.visitor=%223CF0F9940A813A08%22; '
		# 		 'frontend=a1me9sufm8rr0v0p6embf1h495; '
		# 		 'CACHED_FRONT_FORM_KEY=XpTiMcCJcbo7WvP1; '
		# 		 'customerId=; '
		# 		 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221609ae350ba181-04389765f0b032-16386656-2073600-1609ae350bb32a%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%7D%7D; '
		# 		 'preurl=/motherbaby/aaaaa/aeoeaecasaaea.html?is_in_stock=1; '
		# 		 'ucs_ca_i=585; '
		# 		 'ucs_ca=e6cc85b6e8; '
		# 		 'ucs_ca_exp=1514532717; '
		# 		 'CATEGORY_INFO=%7B%22is_in_stock%22%3A%221%22%7D; '
		# 		 'LAST_CATEGORY=6438; '
		# 		 'VIEWED_PRODUCT_IDS=113088%2C109483%2C64467%2C64480%2C109314; '
		# 		 '__xsptplus719=719.12.1514532118.1514533285.7%234%7C%7C%7C%7C%7C%23%23sO9-vHzQ1ZzPsvQ6kekKxfw2WIXjyuK-%23; '
		# 		 'cartItemCount=0; '
		# 		 'loginRet=10; '
		# 		 'scarab.mayAdd=%5B%7B%22i%22%3A%22379395%22%7D%2C%7B%22i%22%3A%22438206%22%7D%2C%7B%22i%22%3A%22698555%22%7D%2C%7B%22i%22%3A%22225304%22%7D%2C%7B%22i%22%3A%22521426%22%7D%2C%7B%22i%22%3A%22101035%22%7D%2C%7B%22i%22%3A%22259128%22%7D%2C%7B%22i%22%3A%2210001525%22%7D%2C%7B%22i%22%3A%22346314%22%7D%2C%7B%22i%22%3A%22201394%22%7D%5D; '
		# 		 'cart_item_count=1; '
		# 		 '_utmc_5bca7a34b3eb077a2787ac2b4998c192=true; '
		# 		 'Hm_lpvt_a3a5d79d073a1c3f23a74df6bc6a6c2c=1514533738',
		# 'Cookie':'_uuid=85D728B9-F3DE-48A9-8158-9DB2B70019F2; '
				 # 'CACHED_FRONT_FORM_KEY=BRn2wghjdacMrp1U; '
				 # 'VIEWED_PRODUCT_IDS=109483; '
				 # 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22160a144f17656e-0576f29b000f18-16386656-1024000-160a144f1774a7%22%7D; '
				 # 'sensorsdata_is_new_user=true; '
				 # 'SERVER_ID=17c3dc44-3892b1f4; '
				 # '__xsptplusUT_719=1; '
				 # 'Hm_lvt_a3a5d79d073a1c3f23a74df6bc6a6c2c=1514534139;'
				 # ' Hm_lpvt_a3a5d79d073a1c3f23a74df6bc6a6c2c=1514534139; '
				 # 'customerId=; '
				 # '__xsptplus719=719.1.1514534139.1514534139.1%234%7C%7C%7C%7C%7C%23%23QAT0NElJX35usNsnv348AFQg9MY89Jva%23; '
				 # 'frontend=hq6c6efuj8ot6lbne3kbth1rc7; '
				 # 'cartItemCount=0; '
				 # 'loginRet=10; '
				 # 'scarab.mayAdd=%5B%7B%22i%22%3A%22346314%22%7D%5D; '
				 # 'scarab.visitor=%223CF0F9940A813A08%22; '
				 # 'cart_item_count=1'
				}
# rrr = requests.get('http://127.0.0.1:5555/random')
# proxy = rrr.text
# print(proxy)
# proxies = {
# 	'http': 'http://' + proxy,
# 	'https': 'https://' + proxy,
# }
# proxies = {
# 		'http':'socks5:localhost:1080',
# 		'https': 'socks5:localhost:1080',
# 	}


def request(method, url, **kwargs):
	# kwargs.setdefault('proxies',proxies)
	kwargs.setdefault('allow_redirects',True)
	kwargs.setdefault('timeout', 30)
	kwargs.setdefault('headers', Headers)
	# kwargs.setdefault('cookies',cookies)
	kwargs.setdefault('verify', False)
	r = SESSION.request(method, url, **kwargs)
	# r.xpath = etree.HTML(r.text).xpath
	return r
#
# data = {
#     'offset':'0',
#     'id_rubrik':'terbaru',
#     'kanal_name':'peluangusaha',
# }
#
# rr = requests.post('http://peluangusaha.kontan.co.id/ajax/more_news',headers=headers,data=data)

# data = {
#     'id_rubrik':43,
#     'kanal_name':'personalfinance'
# }
#
#
# rrr = requests.post('http://personalfinance.kontan.co.id/ajax/more_rubrik')

# data = {
#     'id_berita':'377976',
# }
#
# rr = requests.post('http://personalfinance.kontan.co.id/ajax/autopost_popular_news',headers=headers,data=data)


# def get_response(url):
#     rr= requests.get(url,headers=headers)
#     rr.xpath = etree.HTML(text=rr.text).xpath
#     return rr
#
# rr = get_response('http://personalfinance.kontan.co.id/news/kesalahan-generasi-milenial-dalam-atur-keuangan')
# news_data = rr.xpath('//script[@type="application/ld+json"]/text()')
# news_info = ''
# for new in news_data:
#     if 'NewsArticle' in new:
#         news_info = ''.join([x.strip() for x in new.replace('\r\n','').split(' ')])
# news_json = json.loads(news_info)
#
# print json.dumps(news_json,indent=2)

#
# from collections import OrderedDict
#
# month_map_tmp = {
#     '1':'31',
#     '2':'28',
#     '3':'31',
#     '4':'30',
#     '5':'31',
#     '6':'30',
#     '7':'31',
#     '8':'31',
#     '9':'30',
#     '10':'31',
#     '11':'30',
#     '12':'31'
# }
# order_month_map = OrderedDict(sorted(month_map_tmp.items(),key=lambda x: int(x[0])))
# def sday_to_mday(day):
# 	assert day > 0 and day <= 365
# 	all_days = 0
# 	for month_num, day_num in order_month_map.iteritems():
# 		all_days += int(day_num)
# 		if all_days >= day:
# 			m = month_num
# 			d = int(day_num) - (all_days - day)
# 			if int(m) < 10:
# 				m = '0'+str(m)
# 			if int(d) < 10:
# 				d = '0'+str(d)
# 			return str(m), str(d)
# 		else:
# 			continue
# 	return
#
# def mday_to_sday(m, d):
# 	assert m > 0 and m <= 12
# 	assert d > 0 and d <= int(order_month_map[str(m)])
# 	all_days = 0
# 	for month_num, day_num in order_month_map.iteritems():
# 		if int(month_num) == m:
# 			all_days += d
# 			return all_days
# 		all_days += int(day_num)
# 	return
#
# m,d = sday_to_mday(15)
# dayss = mday_to_sday(12,31)
# print m,d

# def parse():
# 	all_urls = []
# 	index_page = request('GET',"https://cn.pharmacyonline.com.au")
# 	first_categorys = [x for x in index_page.xpath('//div[@id="H-nav"]/ul//li[@class="nav-top"]')
#                        if x.xpath('.//div[contains(@class,"nav-top-contain")]')]
# 	categorys = []
#
# 	for first_category in first_categorys:
# 		first_category_name = first_category.xpath('./a[@class="nav-top-title"]/span/text()')[0]
# 		second_categorys = first_category.xpath('./div[contains(@class,"nav-top-contain")]/div[@class="nav-top-contain-left"]/div[contains(@class,"top-contain-single")]')
# 		for sencond_category in second_categorys:
# 			sencond_category_name = sencond_category.xpath('./h2[@class="top-contain-title"]/a/text()')[0]
# 			third_categorys = sencond_category.xpath('./div[@class="top-contain-item"]/a')
# 			if third_categorys:
# 				for third_category in third_categorys:
# 					sub_category = " | ".join(
# 						[first_category_name, sencond_category_name, third_category.xpath('./text()')[0]])
# 					url = third_category.xpath('./@href')[0]
# 					categorys.append(sub_category)
# 					all_urls.append([url, sub_category])
# 			else:
# 				sub_category = " | ".join([first_category_name, sencond_category_name])
# 				categorys.append(sub_category)
# 				url = sencond_category.xpath('./h2[@class="top-contain-title"]/a/@href')[0]
# 				all_urls.append([url, sub_category])
# 	with open('pharmacyonline_category.txt', 'w', encoding='utf-8') as e:
# 		for category in categorys:
# 			e.write(category+'\n')
	

# rr= request('POST','https://cn.pharmacyonline.com.au/o_exp/index/emarsys')
# parse()
# data = {
# 	'item_id':396405,
# 	'qty':1
# }
# rr = request('POST','https://cn.pharmacyonline.com.au/v2/item/change',data =data)

# rr = request('GET','https://cn.pharmacyonline.com.au/v2/item/add?product_id=109483&qty=1')
# rr = request('GET','https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter')
# with open('taobao.html','wb') as f:
# 	f.write(rr.content)


# def register(username, password, nickname=None):
# 	rr = request('GET','https://www.shopspring.com/signin',headers = Header1)
# 	CSRF = re.findall('_CSRF = \"(.*?)\";',rr.text)[0].replace('\\x2b','+').replace('\\/','/')
# 	csrf_token = rr.cookies['csrf_token']
# 	import ipdb
# 	ipdb.set_trace()
# 	nickname = nickname or (re.findall('\w+', username)[0])
# 	form_params = {
# 		'name': 'ccc bbb',
# 		'email': username,
# 		'password': password,
# 	}
# 	Headers.update({'X-CSRF-Token':CSRF})
# 	cookies = {'csrf_token':csrf_token}
# 	response = request('POST','https://www.shopspring.com/api/1/users/find_or_create',headers=Headers,cookies=cookies, data = form_params)
# 	ipdb.set_trace()
# 	error = response.json()['error']
# 	message = response.json()['message']
# 	human_message = response.json()['human_message']






if __name__ == '__main__':
	# register('727973328@qq.com','cjxh')
	
	rr = request('GET',
				 # 'https://www.macys.com/shop/product/dooney-bourke-kendra-satchel?ID=4922414&intnl=true',
				 'https://www.macys.com/shop/product?ID=4922414',
				 # 'http://www.cjxh616.com'
				 # 'https://store.nike.com/us/en_us/pw/'
				 )
	ipdb.set_trace()
