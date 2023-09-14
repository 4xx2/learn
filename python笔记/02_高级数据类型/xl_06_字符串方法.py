# 是否 空白字符
space_str = "   \t \n \r "
print(space_str.isspace())
# 是否数字
num_str = "12345"
print(num_str.isdecimal())

# 查找和替换
hello_str = "hello world"
# 1.是否以指定字符串开始
print(hello_str.startswith("he"))
# 2.是否以指定字符串结束
print(hello_str.endswith("ld"))
# 3.查找指定字符串
print(hello_str.find("o"))
# 4.替换字符串,replace执行完成后，返回一个新字符串，不修改原有字符串
print(hello_str.replace("world", "python"))
print(hello_str)

# 字符串的拆分与合并
po_str = "1234\ndsfoa\t  dslaf\ndsfal\n"
po_list = po_str.split()
print(po_list)
po_str = " ".join(po_list)
print(po_str)

# 字符串的切片
str_01 = po_str[0:10:2]
str_02 = po_str[::-1]   # 逆序
print(str_01)
print(str_02)


