# def func (a, b, c):
#     print('a = %s' %a)
#     print('b = %s' %b)
#     print('b = %s' %c)
#
# func(1, c = 3 , b = 2)

# 取得参数的个数
def howlong(first, *other):
    print(1 + len(other))

howlong(123, 234, 456)