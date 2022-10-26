import requests
import re
content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text

print(content)

pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)
results = re.findall(pattern, content)
print(results)

for results in results:
    url, name = results
    print(url, re.sub('\s', '', name))
