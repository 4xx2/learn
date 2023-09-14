def print_info(name, title="", gender=True):
    """
    定义缺省参数时，应该放在参数列表的末尾
    缺省参数：在定义缺省参数时，应该使用最常见的值作为默认值
    :param title:
    :param name:学生的姓名
    :param gender:男生True  女生 False
    :return:
    """
    gender_text = "男生"

    if not gender:
        gender_text = "女生"
    print("[%s]  %s 是 %s" % (title, name, gender_text))


# 调用带有多个缺省参数的函数时，需要指定参数名
print_info("小明", gender=True)
print_info("往")
