import xl_08_mutiple_table

# 使用函数，用.
xl_08_mutiple_table.multiple_table()


def sum_2_num(num1, num2):
    """试试"""
    print("%.2f+%.2f = %.2f" % (num1, num2, num1 + num2))
    return num1+num2


num1 = sum_2_num(15, 20.2)
print(num1)


def print_lines(char, times, row):
    """打印分割线

    :param char:分割字符
    :param times:重复次数
    :param row:行数
    """
    i = 0
    while i < row:
        print(char * times)
        i += 1


print_lines("*", 5, 5)
