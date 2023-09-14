t_str = "sdfjanvoqklzqpf"
t_list = [234, 32143, 2341, 657, 341, 57, 123, 94]
t_dict = {"a": 895, "b": 99, "c": 81}

# max min 查看容器中的最大值和最小值
# max min 对字典使用时 仅仅比较key
print(max(t_list))
print(min(t_str))
print(max(t_dict))

# 比较 字典和字典不能比较
print('aaa' > 'bbb')

# 元组和列表都可以切片
print([0, 1, 2, 3, 4][1:3])
print((0, 1, 2, 3, 4)[1:3])

# 运算符
print([1, 2] * 3)
print([1, 2] + [3, 4])
print((1, 3) + (3, 4))
print((1, 2) * 2)
print(3 in [1, 2])
print(2 in (1, 2)) 
