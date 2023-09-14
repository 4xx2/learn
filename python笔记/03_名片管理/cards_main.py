import cards_tools

# 无限循环
while True:
    # TODO 显示功能菜单 TODO 可以醒目提醒
    cards_tools.show_menu()

    action_str = input("请选择操作：")  # input返回字符串
    print("您选择的操作是%s" % action_str)

    # 针对用户的输入，进行的操作
    if action_str in ["1", "2", "3"]:
        # 开发程序时，不希望立即编写
        # 可以用pass关键字，作为一个占位符，保证程序正常执行
        # pass

        # 新增名片
        if action_str == "1":
            cards_tools.new_card()

        # 显示全部
        if action_str == "2":
            cards_tools.show_card()

        # 查询名片
        if action_str == "3":
            cards_tools.search_card()

    elif action_str == "0":
        print("欢迎再次使用")
        break
    else:
        print("您输入的不正确，重新输入")
