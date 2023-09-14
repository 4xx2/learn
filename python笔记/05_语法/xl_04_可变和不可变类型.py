def demo(num, num_list, num_list2):
    """
    无论传递的参数是可变的，还是不可变的
    针对参数使用赋值语句，会在函数内部修改局部变量的引用，不影响外部变量
    如果在函数内部使用方法改变数据内容，会影响外部变量
    :param num_list2:
    :param num:
    :param num_list:
    :return:
    """
    num = 100
    num_list = [1, 2, 3]
    num_list2[1] = 99
    print(num)
    print(num_list)
    print(num_list2)


gl_num = 99
gl_list = [4, 5, 6]
gl_list2 = [7, 8, 9]
demo(gl_num, gl_list, gl_list2)
print(gl_num)
print(gl_list)
print(gl_list2)
