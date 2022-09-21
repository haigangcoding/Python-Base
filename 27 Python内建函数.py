# a = [1, 2, 3, 4, 5, 6, 7]
# list(filter(lambda x: x > 2, a))
# # Out[3]: [3, 4, 5, 6, 7]
#
# a = [1, 2, 3]
# map(lambda x: x, a)
# # <map at 0x1d425b4ac08>
#
# a = [1, 2, 3]
# list(map(lambda x: x, a))
# # Out[7]: [1, 2, 3]
# list(map(lambda x: x + 1, a))
# # Out[8]: [2, 3, 4]
# b = [4, 5, 6]
# list(map(lambda x, y: x + y, a, b))
# # Out[10]: [5, 7, 9]

# from functools import reduce
# reduce(lambda x, y: x + y, [2, 3, 4], 1)
# Out[12]: 10

# zip((1, 2, 3), (4, 5, 6))
# Out[14]: <zip at 0x1d425b54c08>

# for i in zip((1, 2, 3), (4, 5, 6)):
#     print(i)
# (1, 4)
# (2, 5)
# (3, 6)

