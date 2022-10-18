import re

p = re.compile(r'(\d+)-(\d+)-(\d)')
print(p.match('2018-05-10').group(2))
print(p.match('2018-05-10').groups())