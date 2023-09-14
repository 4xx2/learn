"""
不使用其他变量，交换两个变量的值
"""
a = 6
b = 100
# 使用其他变量
# c = a
# a = b
# b = c
# 解法2：不使用其它变量
a = a + b
b = a - b
a = a - b
print(a, b)
# python 专有的解法
# a, b = (b, a) 括号可以省略，等号右边是元组
a, b = b, a
print(a, b)


