import numpy as np

# 产生 0 - 9的整数
arr4 = np.arange(10)

# 打印 arr4
# print(arr4)

# 切片获取第 6 个元素
print(arr4[5])

# 获取 5 - 8的元素
print(arr4[5: 8])

# 赋值5 - 8 的元素 为 10
arr4[5:8] = 10
print(arr4)

# 对数组进行重新赋值，不改变原有数组内容
arr_slice = arr4[5:8].copy()
arr_slice[:] = 15
print(arr_slice)
print(arr4)
