import re

p = re.compile(r'(\d+)-(\d+)-(\d+)')

print(p.search('aa2018-05-10bb'))
phone = '123-456-789 # 这是电话号码'
p2 = re.sub(r'#.*s', '', phone)
print(p2)
p3 = re.sub(r'\D', '', p2)
print(p3)