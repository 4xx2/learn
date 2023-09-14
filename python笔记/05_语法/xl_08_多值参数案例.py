"""
定义一个函数sum_numbers，可以接收任意多个参数
"""


def sum_numbers(*nums):
    result = 0
    for num in nums:
        result += num
    print(result)


sum_numbers(2, 3, 4)
sum_numbers(2, 90, 134, 134)
