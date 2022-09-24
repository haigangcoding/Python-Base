
# # 读取人物名称
# f = open('name.txt', encoding='utf-8')
# data = f.read()
# print(data.split('|'))
#
# # 读取兵器名称
# f2 = open('weapon.txt', encoding='utf-8')
#
# i = 1
# for line in f2.readlines():
#     if i % 2 == 1:
#         print(line.strip('\n'))
#     i += 1
#
# f3 = open('sanguo.txt', encoding='gbk', errors='ignore')
# print(f3.read().replace('\n', ''))

# 函数是对程序逻辑进行结构化的一种编程方法
# 函数的定义
# def 函数名称():
    # 代码
    # return 需要返回的内容
# 函数的调用
#     函数名称()

# def func(filename):
#     print(open(filename).read())
#     print('test func')
#
# func('name.txt')

import re
def find_item( hero ):
    with open('sanguo.txt', encoding='GB18030') as f:
        data = f.read().replace('\n', '')
        name_num = re.findall(hero, data)
        # print('主角 %s 出现 %s 次' %(hero, len(name_num)))
    return len(name_num)

# 读取人物的信息
name_dict = {}
with open('name.txt', encoding='utf-8', errors='ignore') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            name_num = find_item(n)
            name_dict[n] = name_num
