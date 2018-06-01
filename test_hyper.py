import requests
from hyper.contrib import HTTP20Adapter #hyper垃圾
import ipdb
from lxml import etree
import json



headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,zh-TW;q=0.8,ja;q=0.7',
    'Cache-Control':'no-cache',
    'Connection': 'keep-alive',
    # 'cookie':'shippingCountry=CN; SignedIn=0; GCs=CartItem1_92_03_87_UserName1_92_4_02_; mercury=true; SEED=-3158406867929591320%7C89-20%2C76-20; mt.v=2.731512258.1517225440783; _msuuid_qljqreuvj0=B90D1C77-7E6A-4C52-AD02-B162BD5CAB50; RTD=8335bb0833fa0083394a083360208338f50833aec0833de30833cb10; SEGMENT=%7B%22EXPERIMENT%22%3A%5B2816%5D%7D; __utma=83436613.271365623.1517225443.1517225443.1517225443.1; __utmc=83436613; __utmz=83436613.1517225443.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); cmTPSet=Y; mt.urlQuery=(); _caid=99edfb9e-4e60-4200-972e-801f7e670094; _cavisit=16141af042c|; _ga=GA1.2.271365623.1517225443; _gid=GA1.2.274930404.1517225444; ak_bmsc=203C4E0A2F9EBD10A767D03668F9242A6860A964CD240000DE056F5AA8D86900~plkOa9nxXNdf9GnhOKGe/D4LquCZhWk/2XuWaATAyvS8DgKcjTTocxxSn0lVnlVSUTFc30NXJMbk0sQhu27B9dwvWg73nx1rTeAnwXcVr9cOt/QvY+gx/fVuMpI87UmIVelpT2R8wNZgDxda7ZBPiNVtHP9Lwm262eGJI5t5+C2naAF01tzw27LsKRO9GVh7Suu91mVUhjxMswrUKDEP9n3SY/+EcQalPhefvrvs2RrVK0ReRydhnKG2WV+T4GC5jN; _4c_mc_=3a1f09217d9d774c6f957cb6682be1c6; _sp_ses.c359=*; currency=USD; xdVisitorId=13D0rJXb6iG-y_3D6nR1qd9sXZBDVhTTQZJjgGLv6UMp5bw84D0; atgRecVisitorId=13D0rJXb6iG-y_3D6nR1qd9sXZBDVhTTQZJjgGLv6UMp5bw84D0; mbox=session#1517225439774-594355#1517227413|PC#1517225439774-594355.24_13#1518435153|check#true#1517225613; FORWARDPAGE_KEY=https%3A%2F%2Fwww.bloomingdales.com%2Fshop%2Fproduct%2Fpaul-smith-embroidered-dinosaur-baseball-hat%3FID%3D2747067%26CategoryID%3D1000062%26fromPage%3DcontextPage; rr_rcs=eF5jYSlN9kgxMDQySLNI1k1OM0rVNUk2SdRNTjYx0bVMNTVPAfKSU5OSuXLLSjJT-EyNLXUNdQ0Bp_8PSw; dca=DAL; TS0111b70e=0112b7dea09379935b515d88ef4f957ce0ef83dbb03a6649187bc4e31df0008d69959c36a76306682099861c101b8a2dca6a77a5a0; __utmt=1; atgRecSessionId=p6JB3W2Nlj97LzfXd98oKdXJvF5C4YbNTYDOj4mL6jEfit5I3bK4!-2143529984!-1184568531; utag_main=v_id:016141aef55100197fa00360ea9104079001e07100838$_sn:1$_ss:0$_st:1517230302390$ses_id:1517225440595%3Bexp-session$_pn:12%3Bexp-session; __utmb=83436613.10.10.1517225443; _uetsid=_uet0a833523; BCOMGC=636528253078357125%5E823b31d9-e704-e811-8165-0e0bbe56c72c%5E731338b8-ee04-e811-8175-126fe2cada5c%5E0%5E113.215.97.92; _sp_id.c359=9b68335d-e53e-4095-9b60-989fcffe835b.1517225463.1.1517228509.1517225463.02fb4bb1-cd19-49c3-9e42-b0c8142877a0; akavpau_www_www1_bcom=1517228809~id=78b6771fdf4db2107c56e3259e94fd52; TS0132ea28=0112b7dea05e3ed5c2e801dbd484fb644a66d9a6599bb2d4d04bad100712e7bb51f71d32f3; bm_sv=04E1126A5A8551F219DFEA8E509C40FC~sHzH660qjBG/q/KoKNYsxefmI3eqLoKdt5S5WdyLQTZ9QR/xV7dpjWqRIt5GUogY+7N5yHJcJ95H2OFXEzYyYfAGbjdJD0lHUFMj55ywv4nvvGa8d4VhKQrrpqXjuS3oTdzO8zB3GtL88kohRmZPoX66YNGlA/t7SNxt6jVk6gg=',
    # 'Cookie':'shippingCountry=CN;'
    #          'SignedIn=0; '
    #          'GCs=CartItem1_92_03_87_UserName1_92_4_02_; '
    #          'akavpau_www_www1_bcom=1517225819~id=32f35b889f9b4ef0fb9e5b5cc11e0585; '
    #          'TS0132ea28=0112b7dea080f6ee97aa716e0638162aa7a4253f5ae09b4232ec56bf5573411de34bd48343; '
    #          'mercury=true; '
    #          'SEED=292685253752394216%7C89-20%2C76-21; '
    #          'ak_bmsc=3ADAA84565A6642CB0D88149AADB0B766860A964CD2400002E066F5A2666C567~pln6ZBaWi/6BdYw+yigxb7zlqoYWG78tviYxZTIaoNKl1xTDjDxqauPHb+sgT6ZYTla7XrY1HW2KqZCP/xneO2CgCcQM4CxHtQUsPQRHSlvudsQ8r4sYpJebflvcH0d89Sboya75Q7leyoLhsAcD6nad+mMbFcRQKLpnmZAXT/1cem8Z8eWCEYY8rWGvYNuq3bDKtCVlcZNI2OBazZ0KpVc6wopdOz9TblNu9iDTKeWcPlShEhJzGcQNVyEF8PfFoe; '
    #          'FORWARDPAGE_KEY=https%3A%2F%2Fwww.bloomingdales.com%2Fshop%2Fproduct%2Fpaul-smith-embroidered-dinosaur-baseball-hat%3FID%3D2747067%26CategoryID%3D1000062%26fromPage%3DcontextPage; '
    #          'utag_main=v_id:016141b0302c0023b673e32c14dc00052008a00f00bd0$_sn:1$_ss:1$_st:1517227321198$ses_id:1517225521198%3Bexp-session$_pn:1%3Bexp-session; '
    #          'SEGMENT=%7B%22EXPERIMENT%22%3A%5B2816%5D%7D; '
    #          '_msuuid_qljqreuvj0=3F29A3E2-C06E-4A93-BDE8-966F1497470B; '
    #          '__utma=83436613.1670990219.1517225527.1517225527.1517225527.1; '
    #          '__utmc=83436613; '
    #          '__utmz=83436613.1517225527.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); '
    #          'mt.v=2.73758297.1517225529446; '
    #          '_4c_mc_=f67bcffb7207f4761e7571432746a370; '
    #          '_sp_id.c359=f587d5c6-3d07-40fa-8bfb-4a015fc94342.1517225533.1.1517225533.1517225533.5f1d18db-36bc-4d4c-9029-961fcbb877ca; '
    #          'BCOMGC=636528223336978614%5E879b8b0b-e804-e811-815c-bae49a0ac0f5%5E889b8b0b-e804-e811-815c-bae49a0ac0f5%5E0%5E113.215.97.92; '
    #          '_ga=GA1.2.1670990219.1517225527; '
    #          '_gid=GA1.2.671573028.1517225541; '
    #          '_caid=c2e2f594-0f77-4e1b-8951-27f21e1d6621; '
    #          '_cavisit=16141b092cf|; '
    #          'rr_rcs=eF5jYSlN9kixsDQwNU810TUwSUrTNTExsNS1MDFK0k0yNrUwMTY1MTOzTOLKLSvJTOEzNbbUNdQ1BABzvA1W; '
    #          'mt.urlQuery=(CategoryID:"1000062",ID:"2747067",fromPage:contextPage); '
    #          'xdVisitorId=13D0RxqQslSEn62lcXWFODR5NPiyTU59wSjSYnezi2aMKPU7643; '
    #          'atgRecVisitorId=13D0RxqQslSEn62lcXWFODR5NPiyTU59wSjSYnezi2aMKPU7643; '
    #          'atgRecSessionId=s2dBqB6AfdM9KTYWo-gbLSV-lan2iVnMDbDVQkiK9nws2nb51oTE!-2143529984!-1184568531',
    # 'pragma':'no-cache',
    # 'referer':'https://www.bloomingdales.com/international/context',
    'Host':'www.bloomingdales.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0',
    # 'shippingcountry':'CN',
    # 'cookie':'shippingCountry=CN; currency=USD;',
}
ss = requests.Session()
# ss.mount('https://www.bloomingdales.com',HTTP20Adapter())
# gggg = ss.request('GET','https://health.foresee.com/',headers=headers)
# ggg = ss.request('GET','https://brain.foresee.com/state/bloomingdales/3a1f09217d9d774c6f957cb6682be1c6',headers=headers)
# url = 'https://www.bloomingdales.com/api/catalog/v2/products/1745854?_fields=id%2Cname%2Cbrand%2Cprice%2Cavailable%2CdefaultCategoryId%2CprimaryPortraitSource%2Cattributes%2CreviewStatistics%2CproductUrl%2Ccolormap%2Cupcs&active=true'
url = 'https://www.bloomingdales.com/shop/product/sam.-blake-fur-trim-down-coat?ID=1745854&CategoryID=1001520#fn=ppp%3Dundefined%26sp%3D1%26rId%3D120%26spc%3D545%26spp%3D8%26pn%3D1%7C7%7C8%7C545%26rsid%3Dundefined'
gg = ss.request('GET',url,headers=headers)
gg.xpath = etree.HTML(text=gg.text).xpath
info = json.loads(gg.xpath('//script[@id="pdp_data"]/text()')[0])
ipdb.set_trace()