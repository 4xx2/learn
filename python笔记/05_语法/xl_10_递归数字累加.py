def sum_num(num):
    if num == 1:
        return 1
    return num+sum_num(num-1)


a = sum_num(100)
print(a)
