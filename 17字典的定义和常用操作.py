# dict1 = {}
# print(type(dict1))
# dict2 = {'x': 1 ,'y':2}
# dict2['z'] = 3
# print(dict2)

# 记录生肖，根据年份来判断生肖
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

zodiac_name = (
    u'摩羯座', u'水瓶座', u'双鱼座',
    u'白羊座', u'金牛座', u'双子座',
    u'巨蟹座', u'狮子座', u'处女座',
    u'天秤座', u'天蝎座', u'射手座')

zodiac_days = ((1, 20), (1, 29), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# 用户输入出生年月份和日期
year = int(input('请输入年份'))
month = int(input('请输入月份'))
day = int(input('请输入日期'))

n = 0
while zodiac_days[n] < (month, day):
    if month == 12 and day > 23:
        break
    n += 1
print(zodiac_name[n])

# 输出生肖和星座
print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))


