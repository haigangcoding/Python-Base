
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

def func():
    print(open('name.txt').read())
    print('test func')
func()

