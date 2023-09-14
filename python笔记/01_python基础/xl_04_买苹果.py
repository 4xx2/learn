
price = float(input("苹果单价："))
weight = float(input("苹果重量："))

print("苹果价格"+str(price*weight))

# 格式化输出 %.2:小数点后显示几位数
print("苹果单价：%.2f，苹果重量：%.3f，总价格：%.4f" % (price, weight, price*weight))



