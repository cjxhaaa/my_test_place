ccc = open('macys.txt','a')
ccc.write('123'+'\n')
ccc.write('234'+'\n')
ccc.write('345'+'\n')
ccc.close()


bbb = open('macys.txt','r')
m = bbb.readlines()
import ipdb
ipdb.set_trace()