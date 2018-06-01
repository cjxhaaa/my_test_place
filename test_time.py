## 日期，时间戳转换

import time
st = time.strptime('10 Jan 2018 21:00:07.4845'.split('.')[0],'%d %b %Y %H:%M:%S')
print(st)
print((time.time()-time.mktime(st))/86400)


### 转换规则

# time.striptime 日期转时间戳
# time.strftiome 时间戳转日期

# %a weekday简写
# %A weekday全写
# %b month简写
# %B month全写
# %c 适当的日期时间表示？？？
# %d day十进制（月）[01,31]
# %H hour十进制[00,23]
# %I hour十进制[01,12]
# %j day十进制（年）[001,366]
# %m month十进制[01,12]
# %M minute十进制[00,59]
# %p 上午下午[AM,PM]
# %S second十进制[00,61]
# %U week十进制[00,53]
# %x 日期简写表示？？？
# %X 时间简写表示？？？
# %y 不带世纪的年份[00,99]
# %Y 全写的年份[2018]
# %z 时区偏移，从UTC/GMT开始，格式+HHMM，-HHMM，[-23:59,+23:59]
# %Z 时区名称
# %% %字符