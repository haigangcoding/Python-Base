#
# lambda x:x <= (month, day)
#
# def func1(x):
#     return x <= (month, day)
#
# lambda item:item[1]
#
def func2(item):
    return item[1]

adict = {'a': 'aa', 'b': 'bb'}
for i in adict.items():
    func2(i)
