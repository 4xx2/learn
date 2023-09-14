"""
元组与列表类似，但是元组不能修改
元组用（）定义
元组通常保存不同种类的数据
"""
# 定义空元组 tuple = ()
info_tuple = ("张三", 18, 1.75)

print(info_tuple[1])

# 如何定义只有一个元素的元组，括号内只有一个元素定义后并不是元组
# s_tuple = (5)
# print(type(s_tuple))
single_tuple = (5,)
print(type(single_tuple))

# 元组有两个方法，count，index
# index,已经知道值，找该值的位置
print(info_tuple.index(18))
print(info_tuple[2])
print(info_tuple)
print(info_tuple.count(18))
print(len(info_tuple))

# 元组循环遍历,不常用，因为元组中数据类型不一致
for s in info_tuple:
    print(s)

# 元组的应用,使 用   格式化字符串  拼接一个新的字符串
info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple
print(info_str)

# 元组的应用，元组和列表的转换
num = [1, 2, 3]
tuple(num)
print(type(num))
list(info_tuple)
print(type(info_tuple))