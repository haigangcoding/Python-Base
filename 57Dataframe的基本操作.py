from pandas import Series, DataFrame
import pandas as pd


obj = Series([4, 5, 6, -7])

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'c', 'a'])

# 定义一个字典
sdata = {'beijing': 35000, 'shanghai': 71000, 'guangzhou': 16000, 'shenzhen': 5000}
obj3 = Series(sdata)

obj3.index = ['bj', 'gz', 'sh', 'sz']

data = {'city':['shanghai', 'shanghai', 'shanghai', 'beijing', 'beijing'],
        'year': [2016, 2017, 2018, 2017, 2018],
        'pop': [1.5, 1.7,3.6, 2.4, 2.9]}

# frame = DataFrame(data)
#
# frame2 = DataFrame(data, columns=['year', 'city', 'pop'])

# print(frame)
#
# # 提取城市
# print(frame2['city'])
#
# # 提取年份
# print(frame2.year)

# # 增加一列
# frame2['new'] = 100
#
# print(frame2)
#
# # 判断是否是北京 cap
# frame2['Capital'] = frame2.city == 'beijing'
#
# print(frame2)

# pop = {'beijing': {2008: 1.5, 2009: 2.0},
#        'shanghai': {2008: 2.0, 2009: 3.6}
#        },
# frame3 = DataFrame(pop)
# print(frame3.T)

obj4 = Series([4.5, 7.2, -5.3, 3.6], index=['b', 'd', 'c', 'a'])

# 把 fill_value 空值变成零
obj5 = obj4.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)

print(obj5)

# 讲颜色 赋值到 3个索引当中
obj6 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])

# reindex 讲索引进行重新制定
# :采用ffill()函数沿索引轴填充缺失值
print(obj6.reindex(range(6), method='ffill'))

from numpy import nan as NA

data = Series([1, NA, 2])

data2 = DataFrame([[1, 6.5, 3], [1, NA, NA], [NA, NA, NA]])

data2[4] = NA
# axis删除一整列的参数
print(data2)
print(data2.dropna(axis=1, how='all'))

# 将 NAN 替换为 0
data2.fillna(0)
print(data2.fillna(0, inplace=True))
print(data2)
