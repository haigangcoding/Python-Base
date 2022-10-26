# 网络库 1. urllib 库           http协议常用库
#       2. requests 库         http 协议常用库
#       3. BeautifulSoup 库    xml 格式处理库

from urllib import request

url = "http://www.baidu.com"
resource = request.urlopen(url, timeout=1)

print(resource.read().decode('utf-8'))
