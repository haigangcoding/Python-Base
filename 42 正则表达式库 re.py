# 日常应用广泛的模块是：
# 1. 文字处理的 re
# 2. 日期类型的 time datetime
# 3， 数字和数字类型的 math random
# 4. 文件和目录访问的pathlib  os.path
# 5. 通用操作系统的os logging argparse
# 6. 多线程的threading queue
# 7. 数据压缩和归档的 tarfile
# 8. internet 数据处理的 base64 json urllib
# 9. 结构化标记处理工具 html xml
# 10. 开发工具的 unitest
# 11. 调试工具的 timeit
# 12. 软件包发布的 venv
# 13. 运行服务的 __main__

import re
# p = re.compile('a')
# print(p.match('k'))

p = re.compile('ca*t')
print(p.match('caaaaat'))
