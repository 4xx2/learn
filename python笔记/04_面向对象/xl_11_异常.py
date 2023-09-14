# 根据错误类型捕获异常
try:
    # 提示输入整数
    num = int(input("输入一个整数："))

    result = 8 / num

    print(result)
except ZeroDivisionError:
    print("除0错误")
except ValueError:
    print("值错误")
except Exception as result:
    print("未知错误 %s" % result)
else:
    # 没有错误时 执行的代码
    print("没有异常")
finally:
    # 无论是否出现异常，都会执行
    print("结束")


# 主动抛出异常 raise关键字
def input_password(password):
    if len(password) < 8:
        ex = Exception("密码长度不够")
        raise ex
    else:
        return password


try:
    pWord = input("输入密码：")
    print(input_password(pWord))
except Exception as result:
    print("%s" % result)