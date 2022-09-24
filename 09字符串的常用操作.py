# 序列的基本操作
# 成员关系操作符 (in, not in)  对象[not] in 序列
# 连接操作符    （+）          序列 + 序列
# 重复操作符    （*）          序列 * 整数
# 切片操作符    ([])          序列[0:整数]

# 记录生肖，根据年份来判断生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
year = 2018
print(year % 12)
print(chinese_zodiac[year % 12])
print('狗' not in chinese_zodiac)
print(chinese_zodiac + chinese_zodiac)
print(chinese_zodiac + 'abcd')
print(chinese_zodiac * 3)
