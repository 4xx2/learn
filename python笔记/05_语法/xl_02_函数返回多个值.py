"""
函数返回多个值
接受返回元组的方式
"""


def measure():
    print("测量温度")
    temp = 39
    wetness = 49
    # 如果函数返回元组时，可以省略小括号
    return temp, wetness


result = measure()
print(result)

# 如果函数返回的时一个元组，同时希望单独处理元组中的元素
# 可以使用多个变量 一次性接收函数的返回结果
# 注意，使用多个变量接收结果时，应该保证变量个数和元组中元素数量一致
gl_temp, gl_wetness = measure()
print(gl_temp)
print(gl_wetness)
