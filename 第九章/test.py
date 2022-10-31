user_list = [{"name": "ll1", "age": "21"}, {"name": "ll2", "age": "22"}]


def show_stu_info():
    print("-----学生信息列表-----")
    i = 0
    for stu in user_list:
        i += 1
        print(f"{i} {stu['name']} {stu['age']}")
    print("-------------------")


show_stu_info()
