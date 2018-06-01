import ipdb

goods_info_in_page = [{'sku': 'B019YM0E8C', 'price': 2093, 'quantity': 1}, {'sku': 'B019YM0EQE', 'price': 2093, 'quantity': 2}, {'sku': 'B019YM0EQE', 'price': 2093, 'quantity': 2}, {'sku': 'B019YM0E8C', 'price': 2093, 'quantity': 2}, {'sku': 'B019YM0EQE', 'price': 2093, 'quantity': 1}]

compare_goods_map = {}
for _goods in goods_info_in_page:
    if _goods['sku'] not in compare_goods_map:
        compare_goods_map.setdefault(_goods['sku'],{'quantity':_goods['quantity'],'price':_goods['price']})
    else:
        compare_goods_map[_goods['sku']]['quantity'] += int(_goods['quantity'])
goods_info_in_page = []
for _k,_v in compare_goods_map.iteritems():
    goods_info_in_page.append({
        'sku':_k,
        'price':_v['price'],
        'quantity':_v['quantity']
    })
ipdb.set_trace()