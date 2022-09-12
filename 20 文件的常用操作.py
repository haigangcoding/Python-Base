# coding = utf8
# file4 = open('name.txt')
# print(file4.readline())
#
# file5 = open('name.txt')
# for line in file5.readlines():
#     print(line)
#     print('====')

file6 = open('name.txt')

print(file6.tell())
file6.read(1)
print(file6.tell())
