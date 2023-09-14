class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s 占地 %.2f" % (self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积 家具名称列表
        self.free_area = area
        self.item_list = []

    def add_item(self, item):
        print("增加%s" % item)
        # 判断家具是否可以添加进入房子
        if item.area>self.free_area:
            print("面积太大无法添加")
            return
        self.free_area -= item.area
        self.item_list.append(item.name)

    def __str__(self):
        # python会自动把括号内的代码连接在一起
        return ("房子户型是%s 总面积是%.2f \n剩余面积是%.2f \n包括的家具有%s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))


# 创建家具
yi_gui = HouseItem("衣柜", 20)
# 创建房子
house = House("两室一厅", 120)
# 添加家具
house.add_item(yi_gui)
print(house)
