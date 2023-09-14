# 定义字典用{}
xm_dict = {"name": "小明",
           "age": 18,
           "height": 1.75,
           "gender": True,
           "weight": 75}
print(xm_dict)

# 增删改查
print(xm_dict["name"])  # 查
xm_dict["age"] = 18  # 增
xm_dict["name"] = "小名"  # 改
print(xm_dict)
xm_dict.pop("name")  # 删
print(xm_dict)

# 统计  键值对  数量
print(len(xm_dict))
# 合并字典,如果被合并的字典中包含已经存在的  键值对 ，会覆盖原有的键值对
temp_dict = {"name": "xm"}
xm_dict.update(temp_dict)
print(xm_dict)

# 清空字典
xm_dict.clear()
print(xm_dict)

xm_dict = {'name': "小明",
           'age': 18,
           'height': 1.75}
# 遍历字典
for k in xm_dict:
    print("%s : %s" % (k, xm_dict[k]))

# 字典应用 将多个字典合并到一个列表中，列表遍历 进行同样的操作
card_list = [
    {"name": "张三", "qq": "123", "phone": "345"},
    {"name": "李四", "qq": "354", "phone": "231"}
]
for card_info in card_list:
    print(card_info)