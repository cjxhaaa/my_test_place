import requests,json,ipdb
# from requests.exceptions import ProxyEresponseor


# headers = {"Accept": "*/*",
#            # "Accept-Encoding":"gzip, deflate, br",
#            "Accept-Language":"en-US,en;q=0.5",
#            # "Connection":"keep-alive",
#            # "Content-Length":"1551",
#            "content-type":"application/json",
#            # "Cookie":'isMobile=false; isTablet=false; _abck=F90B4BFD3B2C1410FE7F7FDD39B898D617D4326AAF7800003FA8285ACE6EFC36~0~D/yDI5OqYL8VxhTPdB77mD+ilUkw71lp0uqGBtzguNU=~-1~-1; bm_sz=2C7D05CF45BD2DB9F7CC6EB337B79D04~QAAQajLUF+y3PyVgAQAAalzRLjDVJQN9SRG4s048NyebwZMBJYheD9eTDQfsiGlohPw+bQhjEHQ8fF1U/YokF3xe8eqU7pD80DBKpsqH1APqmEandymIXPSGc1OypYe6qIJrvs3tpbgs1/e6V78dgwresponse/rZuSOU6KKxFX5vAC6UznTee+Fd4/DynLiE7KF46; siteType=A; closedEmailPromo=true; EXTERNAL_HOST=origin-www.express.com; JSESSIONID=BDBFFA603E05B99F9892BAD43D33C3F5.cmhlpecomecm09w2; customerGroupType=1; bagCount=1; exp_hbeat=1; mmapi.p.pd=%22-743267677%7CCgAAAApVAgCwcjQvmQ8AAREAAULEExRIAgAvWD%2FTIj3VSHX2PsgaPdVIAAAAAP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FAAZEaXJlY3QBmQ8CAAAAAAAAAAAAS%2BoAAEvqAABL6gAAAgB7swAADj7Yc%2FeZDwD%2F%2F%2F%2F%2FAZkPmQ%2F%2F%2FwQAAAAAAAAAAZGZAQBfhQIAAEqtAACwG4p8uZkPAP%2F%2F%2F%2F8BmQ%2BZD%2F%2F%2FAQAAAQAAAAAB3owBABJeAgAAAAAAAAABRQ%3D%3D%22; mmapi.p.srv=%22lvsvwcgus09%22; gig_hasGmid=ver2; _sr_sp_ses.3650=*; _sr_sp_id.3650=d3001c9a-bc7c-4955-8e2b-e2a3c0ae0fe0.1512613966.1.1512617405.1512613966.93c5f236-9124-4d37-9a54-aaca1b193126; sr_pik_session_id=6b27e897-797c-da74-3262-77ab336e5565; sr_browser_id=bca07fdc-77bf-4f18-abed-64e22028ffd4; rkglsid=h-b7bd57077b1a6b075fe101001602ed17_t-1512617391; btpdb.ACs0xLl.X2J0X3FjX2R1cmF0aW9u=eA; unbxd.userId=uid-1512613971580-97442; unbxd.visitId=visitId-1512613971589-33801; _cplid=a22efe41dc20d39681684527b4470491602ed18a41; granify.uuid=20904820-0880-4060-8800-804050a85028; granify.last_session.1447=1512613972739; granify.session.1447=1512613972739; granify.session_init.1447=1; _ga=GA1.2.965296027.1512613974; _gid=GA1.2.805035747.1512613974; RT="dm=express.com&si=a71fed88-c7bc-44e6-9ec9-f1ff81bd591e&ss=1512613968539&sl=11&tt=2209237&obo=4&sh=1512617397172%3D11%3A4%3A2209237%2C1512617375950%3D10%3A4%3A2188014%2C1512616957828%3D9%3A4%3A341342%2C1512616945192%3D8%3A4%3A341251%2C1512616922426%3D7%3A4%3A341173&bcn=%2F%2F36fb619d.akstat.io%2F&ld=1512617397172&r=https%3A%2F%2Fwww.express.com%2Fclothing%2Fmen%2Fcontrast-heel-toe-dress-socks%2Fpro%2F04602482%2Fcolor%2FRED&ul=1512617405936&hd=1512617406250"; AMCV_5F17123F5245B46D0A490D45%40AdobeOrg=-227196251%7CMCMID%7C91486564800971037498335416394601185715%7CMCAID%7CNONE%7CMCOPTOUT-1512621180s%7CNONE%7CMCAAMLH-1513218780%7C11%7CMCAAMB-1513218780%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; __CT_Data=gpv=7&ckp=tld&dm=express.com&apv_3008_www27=7&cpv_3008_www27=7; __qca=P0-401088453-1512613977824; AMCVS_5F17123F5245B46D0A490D45%40AdobeOrg=1; s_pers=%20c19%3D1512617394233%7C1607225394233%3B%20c19_s%3DLess%2520than%25201%2520day%7C1512619194233%3B%20s_vnum%3D1515205978269%2526vn%253D2%7C1515205978269%3B%20s_invisit%3Dtrue%7C1512619194235%3B%20c5%3DMens%2520%253A%2520Product%2520Detail%2520%253A%2520contrast%2520heel%2520toe%2520dress%2520socks%7C1512619194236%3B; s_cc=true; s_sq=%5B%5BB%5D%5D; _tq_id.TV-81900981-1.3650=dbb399c06cb4ce35.1512613987.0.1512617391..; __bc_audience_sync=%7B%22lastSyncTime%22%3A1512613989229%2C%22audiences%22%3A%5B%5D%7D; s_sess=%20s_ppvl%3DMens%252520%25253A%252520Accessories%252520%25253A%252520Ties%252C7%252C7%252C925%252C1569%252C925%252C1920%252C1080%252C1%252CP%3B%20s_ppv%3DMens%252520%25253A%252520Accessories%252520%25253A%252520Ties%252C7%252C7%252C925%252C1569%252C925%252C1920%252C1080%252C1%252CP%3B; UsrLoginStats=false; anonymOrder=EXPR490841177CMH; _uetsid=_uet6188f1f8; unbxd.visit=repeat; _gat=1; mp_express_mixpanel=%7B%22distinct_id%22%3A%20%221602ed192f2576-0c7daf8fbc1bfc-49566e-1fa400-1602ed192f3595%22%7D',
#            # "Host":"www.express.com",
#            "origin":"https://www.express.com",
#            "Referer":"https://www.express.com/clothing/men/contrast-heel-toe-dress-socks/pro/04602482/color/RED",
#            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0",
#            "x-exp-request-id":"a484302f-2f20-435f-9e7f-b409b3f67933",
#            # "x-exp-rvn-cache-key":"790c1aa9cb4d2aebfa2b203051800561b360608e5876df9c8fee018c18feb181",
#            "x-exp-rvn-cacheable":"false",
#            "x-exp-rvn-query-classification":"product"
# }
#
# j = {'query':'query ProductQuery($productId: String!) { product(id: $productId) { bopisEligible collection crossRelDetailMessage crossRelProductURL fabricCare gender internationalShippingAvailable listPrice name onlineExclusive onlineExclusivePromoMsg productDescription { type content __typename } productId productImage productInventory productURL promoMessage recsAlgorithm salePrice breadCrumbCategory { categoryName h1CategoryName links { rel href __typename } breadCrumbCategory { categoryName h1CategoryName links { rel href __typename } __typename } __typename } colorSlices { color defaultSlice ipColorCode swatchURL imageMap { LARGE __typename } skus { backOrderable displayMSRP displayPrice skuId sizeName inventoryMessage onlineInventoryCount inStoreInventoryCount sizeExtension1 sizeExtension2 __typename } __typename } relatedProducts { listPrice name productId productImage productURL salePrice __typename } __typename  }}',
#      'variables':{'productId':'04602482'},
#      'operationName':'ProductQuery'
#      }
# payload = json.dumps(j)
#
# response = requests.post('https://www.express.com/graphql',headers=headers,data=payload)




# proxy = '41.159.26.123:3128'



# headers1 = {
#     "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#     "Accept-Encoding":"gzip, deflate, br",
#     "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8",
#     "Cache-Control":"no-cache",
#     "Connection":"keep-alive",
#     "Cookie":'isMobile=false; isTablet=false; unbxd.userId=uid-1512614500565-84631; _abck=FC16F0D9E9ECA6BA33D1D0A37A4E7826173DC3B93277000060AA285A3D77F22F~0~cPVnycS5H/4JsFverEuxlMSOHB9dO0wiyaiaiunWxfs=~-1~-1; btpdb.ACs0xLl.X2J0X3FjX2R1cmF0aW9u=eA; __qca=P0-1047410214-1512614513735; granify.uuid=c0e070b8-90c8-40f0-b8d8-68b068301888; _cplid=69c40d0c2d3b8a9e3cfd288d78be8c9c1602ed9db4f; AMCVS_5F17123F5245B46D0A490D45%40AdobeOrg=1; sr_browser_id=f5459bb5-d5fd-4adc-b7af-b85b5f414cdd; anonymOrder=EXPR490820295CMH; UsrLoginStats=false; liveagent_oref=; liveagent_sid=52ba0e71-a55f-433f-9663-a85b6d5fe640; liveagent_vc=2; liveagent_ptid=52ba0e71-a55f-433f-9663-a85b6d5fe640; s_sq=%5B%5BB%5D%5D; s_sess=%20s_ppvl%3DMens%252520%25253A%252520Shirt%252520Shop%252520%25253A%252520Casual%252520Shirts%252C3%252C3%252C379%252C1707%252C379%252C1920%252C1080%252C1%252CP%3B%20s_ppv%3DMens%252520%25253A%252520Shirt%252520Shop%252520%25253A%252520Casual%252520Shirts%252C3%252C3%252C419%252C1707%252C379%252C1920%252C1080%252C1%252CP%3B; granify.last_session.1447=1512624802624; bm_sz=4747B945B80B30CDDDAD42D4A59E2B68~QAAQajLUF07GPyVgAQAAvzW3L9jYLuBKwIJp/WssK0/nC5M9z2J+UsZ8chENrB5tXFQGMkDJW8HxqhrNbKLud+DVex210RLSSJZLbTVtgzUY4Pt3aycKn0CuvBQCUe+DjxZ5stelx+gNZ0NfBvxgETCkKm480fOaZpoE9L+VNR0Ey7/sNp2N3jbnNn08tN0=; JSESSIONID=F608DF967BCBA805A9F82E21F978E25B.cmhlpecomecm08w2; gig_hasGmid=ver2; _ga=GA1.2.682521404.1512614515; _gid=GA1.2.518601557.1512614515; unbxd.visit=repeat; unbxd.visitId=visitId-1512627542645-66018; _uetsid=_ueta5035a5e; rkglsid=h-1f32841b7b1a6b63735afa491602ee26_t-1512632877; mp_express_mixpanel=%7B%22distinct_id%22%3A%20%221602ed9db62573-0368c677a144ed-173b6d56-1fa400-1602ed9db63a89%22%7D; __bc_audience_sync=%7B%22lastSyncTime%22%3A1512632879467%2C%22audiences%22%3A%5B%5D%7D; s_pers=%20s_vnum%3D1515206517749%2526vn%253D3%7C1515206517749%3B%20c19%3D1512632879493%7C1607240879493%3B%20c19_s%3DLess%2520than%25201%2520day%7C1512634679493%3B%20s_invisit%3Dtrue%7C1512634679501%3B%20c5%3DMens%2520%253A%2520Product%2520Detail%2520%253A%2520classic%2520fit%2520easy%2520care%2520textured%25201MX%2520shirt%7C1512634679504%3B; s_cc=true; AMCV_5F17123F5245B46D0A490D45%40AdobeOrg=-227196251%7CMCMID%7C77341419484887114055257852665967121099%7CMCAID%7CNONE%7CMCOPTOUT-1512640079s%7CNONE%7CMCAAMLH-1513219320%7C9%7CMCAAMB-1513237679%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; _tq_id.TV-81900981-1.3650=0741a2066b25e52b.1512614517.0.1512632880..; __CT_Data=gpv=21&ckp=tld&dm=express.com&apv_3008_www27=21&cpv_3008_www27=21; WRIgnore=true; _sr_sp_id.3650=4379b80f-1cde-46e0-b6a1-171d57a1ab4d.1512614824.2.1512632897.1512618391.72a2b360-4535-4ace-882f-184d50bfc10e; _sr_sp_ses.3650=*; granify.session.1447=1512624802624; granify.session_init.1447=1; RT="dm=express.com&si=96f07841-3048-4e8e-946a-1ecf0a0ce94c&ss=1512631960043&sl=1&tt=0&obo=1&sh=1512633245500%3D1%3A1%3A0&bcn=%2F%2F364bf52d.akstat.io%2F&ld=1512633245500&r=https%3A%2F%2Fwww.express.com%2Fclothing%2Fwomen%2Fthermal-bell-sleeve-covertoup%2Fpro%2F08419753%2Fcolor%2FCOWHIDE&ul=1512633245503&hd=1512633245610"; mmapi.p.pd=%22-1661013676%7CHwAAAApVAgDU9NwsmQ8AAREAAUJXl7tvBADkdJG8SD3VSDYZTQocPdVIAAAAAP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FAAZEaXJlY3QBmQ8EAAAAAAAAAAAAS%2BoAAEvqAABL6gAAAQB7swAAqucmdc2ZDwD%2F%2F%2F%2F%2FAZkPmQ%2F%2F%2FxEAAAEAAAAAAZGZAQBfhQIAAAAAAAAAAUU%3D%22; mmapi.p.srv=%22lvsvwcgus08%22; siteType=A; closedEmailPromo=true; EXTERNAL_HOST=www.express.com; customerGroupType=6; bagCount=0; exp_hbeat=1',
#     "Host":"www.express.com",
#     "Pragma":"no-cache",
#     "Referer":"https://www.google.com.hk/",
#     "Upgrade-Insecure-Requests":"1",
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
# }


def get_response():
    proxy = requests.get('http://localhost:5555/random').text.strip('\r')
    print(proxy)
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy,
    }
    try:
        response = requests.get("https://www.express.com/",proxies=proxies,verify=False,timeout=10)
        if response.status_code == 200 and response.text != None:
            return response
        else:
            return get_response()
    except Exception as e:
        print(e)
        return get_response()

if __name__ == "__main__":

    print(get_response().text)
    import hyper
