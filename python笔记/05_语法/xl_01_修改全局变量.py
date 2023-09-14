"""
全局变量的定义规则：不同公司不同要求，加g_或者gl_
"""

num = 10


def demo1():
    # 使用global 可以在函数内部修改全局变量
    global num
    num = 100
    print(num)
    print("%s" % tittle)  # 在开发时应该把所有全局变量定义到所有函数上方，以便正常使用


tittle = "12334"

demo1()
