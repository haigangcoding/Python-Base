import os

# 输出当前路径
print(os.path.abspath('.'))

# 输出相对路径的上一级目录
print(os.path.abspath('..'))

# 判断一下 根目录下的文件是否存在
print(os.path.exists('/Users'))

# 判断一下 是否是文件
print(os.path.isfile('/Users'))

# 是否是目录
print(os.path.isdir('/User'))

