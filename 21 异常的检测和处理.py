# 异常是在出现错误时采用正常控制流以外的动作
# 异常处理的一般流程是:检测到错误,引发异常;对异常进行捕获的操作
# try:
#     <监控异常>
# except Exception[, reason]:
#     <异常处理代码>
# finally:
#     <无论异常是否发生都执行>
# year = int(input('input year:'))
# try:
#     year = int(input('input year:'))
# except ValueError:
#     print('年份要输入数字:')

# a = 123
# a.append()

try:
    a = open('name.txt')
except Exception as e:
    print(e)
finally:
    a.close()
