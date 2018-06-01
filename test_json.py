import json
import ipdb
import re





def json_loads(str):
    t = re.sub('&#039;', '\'', str)
    t = re.sub('\t', ' ', t)
    return json.loads(t)


with open('t.json','r') as e:
    new_e = e.read()


    print(json_loads(new_e)['productDetail'])