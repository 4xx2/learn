# for循环 ， else在循环执行完之后会执行
for num in [1, 2, 3]:
    print(num)
    # break
else:
    # 如果break结束了循环，不执行else
    print("执行")

student1 = {"name": "pter", "age": 18}
student2 = {"name": "rise", "age": 15}
stud_list = [student1, student2]

for stu_dict in stud_list:
    print(stu_dict)
    if stu_dict["name"] == "pter":
        print("ok")
        break
else:
    print("no find")
