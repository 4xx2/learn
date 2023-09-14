
# eval 可以把字符串当作有效的表达式 输出结果
# 不要滥用eval
# eval中输入  __import__('os').system（‘ls') 用户能直接执行终端命令
input_str = input("计算")
print(eval(input_str))

eval(__import__('os').system(input()))
