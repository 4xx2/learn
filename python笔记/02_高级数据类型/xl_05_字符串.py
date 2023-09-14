str1 = "hello python hello"
print(str1[6])    # 字符串也可以索引下标

for char in str1:
    print(char, end="")

"""查
统计字符串长度len
统计一个子字符串  在字符串出现次数count
某一个字符串出现的位置
"""
print(len(str1))
print(str1.count("llo"))
print(str1.index("py"))

