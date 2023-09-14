# 记录所有名片字典
card_list = []


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用名片管理系统")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("0.退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1.输入名片信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入qq：")
    email_str = input("请输入邮箱：")
    # 2.使用信息建立字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
    # 3.将字典添加到列表中
    card_list.append(card_dict)
    # 4.提示用户成功
    print("添加 %s 的名片成功" % card_dict["name"])


def show_card():
    """显示所有名片"""
    # 判断是否有内容,return后面的函数内容不会执行
    if len(card_list) == 0:
        print("没有名片")
        return
    # 打印表格
    print("-" * 50)
    print("显示名片")
    # 打印表头,自定义format输出,中文空格的编码为chr(12288)
    tbtp = "{:<10}\t{:<10}\t{:<10}\t{:<10}"
    print(tbtp.format("姓名", "电话", "qq", "邮箱",
                      chr(12288)))
    # 遍历名片列表
    for card in card_list:
        print(tbtp.format(card["name"],
                          card["phone"],
                          card["qq"],
                          card["email"],
                          chr(12288)))
    print("_" * 50)


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    if len(card_list) == 0:
        print("没有名片")
        return
    # 1.提示用户输入姓名
    name_str = input("输入姓名：")
    # 2.遍历名片列表查找，没找到提示用户
    for card_dict in card_list:
        if card_dict["name"] == name_str:
            # 打印表头,自定义format输出,中文空格的编码为chr(12288)
            tbtp = "{:<10}\t{:<10}\t{:<10}\t{:<10}"
            print(tbtp.format("姓名", "电话", "qq", "邮箱",
                              chr(12288)))
            # 打印具体信息
            print(tbtp.format(card_dict["name"],
                              card_dict["phone"],
                              card_dict["qq"],
                              card_dict["email"],
                              chr(12288)))
            # 修改名片
            amend_card(card_dict)
    else:
        print("没找到")


def amend_card(card_dict):
    """
处理查找到的名片
    :param card_dict: 查找到的名片值
    """
    while True:
        ex_str = input("请输入对名片的操作："
                       "1：修改、2：删除、0：返回上级菜单")
        if ex_str == "1":
            print("直接回车代表不修改")
            card_dict["name"] = input_card_info(card_dict["name"],
                                                "姓名：")
            card_dict["phone"] = input_card_info(card_dict["phone"],
                                                 "电话：")
            card_dict["qq"] = input_card_info(card_dict["qq"],
                                              "qq:")
            card_dict["email"] = input_card_info(card_dict["email"],
                                                 "邮箱：")
            print("修改完成")
        elif ex_str == "2":
            card_list.remove(card_dict)
            print("已删除")
        elif ex_str == "0":
            break
        else:
            print("输入错误，重新输入")


def input_card_info(dict_value, in_str):
    """输入名片信息
    :param dict_value:字典原有的值
    :param in_str:输入提示文字
    :return:如果用户输入内容则返回内容，否则返回原有字典值
    """
    # 1.提示用户输入内容
    input_info = input(in_str)
    # 2.针对用户输入，如果输入内容则返回结果，没有输入返回字典原有值
    if len(input_info) > 0:
        return input_info
    else:
        return dict_value


