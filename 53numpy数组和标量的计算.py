import numpy as np

# arr1 = np.array([2, 3, 4])
#
# arr2 = np.array([1.2, 2.3, 3.4])
#
# print(arr1 + arr2)
# print(arr2 * 10)

# 二维数组
# data = [[1, 2, 3], [4, 5, 6]]
# arr3 = np.array(data)
# print(arr3)
# print(arr3.dtype)

# 定义一个全为 0 的矩阵
print(np.zeros((3, 5)))

# 定义一个全为 1 的矩阵
print(np.ones((4, 6)))

# 矩阵弄成空值
# numpy.empty()函数
# 这个函数可以创建一个没有任何具体值的ndarray数组，是创建数组最快的方法
print(np.empty((2, 3, 2)))
