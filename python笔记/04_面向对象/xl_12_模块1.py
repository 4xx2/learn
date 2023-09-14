def say_hello():
    print("hello,模块1")


class Dog:
    def __init__(self, name):
        self.name = name

    def dark(self):
        print("%s" % self.name)


# 直接执行的代码，在被导入时会直接执行
# 导入文件时 模块中没有缩进的代码都会被执行一次
print("开发的模块")

# 直接输出__name__ 就是固定的__main__
# 导入文件时，输出的是 模块名
print(__name__)


# 如果导入文件时，不需要执行的代码，可以如下操作
#  使用main函数做测试
def main():
    say_hello()
    print("导入文件后，不执行")
    say_hello()


if __name__ == "__main__":

    main()
