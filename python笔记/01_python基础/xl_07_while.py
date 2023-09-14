i = 1

while i <= 5:
    print("hello")
    i = i+1

# 累计求和
i = 0
a = 0
while i <= 100:
    a += i
    i += 1
print(a)

# 累计求和
i = 0
a = 0
while i <= 100:
    a += i
    i += 2
print(a)

# 打印小**
row = 1
while row <= 5:
    print("*" * row)
    row += 1

row = 1
while row <= 5:
    i = 1
    while i <= row:
        print("*", end="")
        i += 1
    print("")
    row += 1

# 乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%d" % (i, j, i*j), end="\t")
        j += 1
    print("")
    i += 1



