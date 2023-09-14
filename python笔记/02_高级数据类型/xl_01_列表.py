name_list = ["张三", "李四", "王五"]

# 取值
print(name_list[1])

# 找数据在什么位置 index
# 找不到会报错
print(name_list.index("张三"))
# print(name_list.index("张三三十"))

# 修改数据，超出范围报错
name_list[1] = "张三改"
# name_list[3] = "li"

# 增加数据 append追加，insert插入，extend扩展
# append可以向末尾添加数据,添加的是一个列表时，列表作为一个整体添加
name_list.append("赵六")
name_list.append([1, 2])
print(name_list)
# insert
name_list.insert(2, "1234")
# extend 把其他列表内容追加到末尾，天剑列表时，列表合并到原列表
temp_list = [1, 2, 3]
name_list.extend(temp_list)
print(name_list)

""" 删除 remove删除指定的第一次出现的数据，
pop默认删除最后一个元素（相当于栈）
pop方法可以指定要删除元素的索引
clear方法清空列表
del 关键字本质上是用来将一个变量从内存中删除的，删除后，后续就不能使用了
"""
name_list.remove("王五")
name_list.pop()
name = name_list.pop(2)
print(name)
print(name_list)
name_list.clear()
print(name_list)
name_list = ['张三', '张三改', '1234', '王五', '赵六', 1, 2, 3]
print(name_list)
# del name_list
# print(name_list) # 会报错，已经删除name_list

"""len函数统计列表元素个数
count 方法可以统计列表中某个数据出现次数
"""
print("列表中包含%d个元素" % len(name_list))
print("张三出现了%d次" % name_list.count("张三"))

"""排序：sort ; 翻转：reverse
sort默认正序，输入reverse=TRUE 为逆序

"""
num_list = [3, 4, 6, 7, 5, 1, 2, 3, 6, 3, 8, 9, 0]
# num_list.sort()
print(num_list)
# num_list.sort(reverse=True)
# print(num\Python\02_高级数据类型\venv\Scripts\python.exe D:/Python/02_高级数据类型/xl_01_列表.py
# 李四
# 0
# ['张三', '张三改', '1234', '王五', '赵六', 1, 2, 3]
# 1234
# ['张三', '张三改', '赵六', 1, 2]
# []
# ['张三', '张三改', '1234', '王五', '赵六', 1, 2, 3]
# 列表中包含8个元素
# 张三出现了1次
# [3, 4, 6, 7, 5, 1, 2, 3, 6, 3, 8, 9, 0]
# [0, 9, 8, 3, 6, 3, 2, 1, 5, 7, 6, 4, 3]
# [3, 2, 1, '赵六', '王五', '1234', '张三改', '张三']_list)
name_list.reverse()
num_list.reverse()
print(num_list)
print(name_list)

