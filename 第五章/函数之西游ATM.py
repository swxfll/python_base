# 定义全局变量
account_money = 10000
user_name = None


# 定义主菜单
def menu():
    print("---------------主菜单-----------")
    print(f"{user_name}, 你好, 欢迎来到西游ATM, 请选择你的操作:")
    print("查询余额 [输入1]")
    print("存款    [输入2]")
    print("取款    [输入3]")
    print("退出    [输入4]")

    return int(input("请输入您的选择"))


# 定义查询函数
def query(show_header):
    if show_header:
        print("---------------查询余额-----------")
    print("%s, 你好, 你的账户余额是: %d" % (user_name, account_money))


# 定义存款函数
def saving(num):
    global account_money

    print("---------------存款-----------")
    account_money += num
    print(f"成功存入{num}元, 账户余额{account_money}")

    # 调用query函数查询余额
    query(False)


# 定义取款函数
def get_money(num):
    global account_money
    account_money -= num
    print("---------------取款-----------")
    print(f"成功取出{num}, 账户余额{account_money}")

    # 调用query函数查询余额
    query(False)


while True:
    user_input = menu()
    if user_input == 1:
        query(True)
        continue
    elif user_input == 2:
        num = int(input("请输入存款余额: "))
        saving(num)
        continue
    elif user_input == 3:


user_name = input("请输入你的姓名: ")

# while True:
#     select = menu(user_name)
#     if select == 1:
#         print("---------------查询余额-----------")
#         print("%s, 你好, 你的账户余额是: %d" % (user_name, account_money))
#     elif select == 2:
#         num = int(input("请输入你要存钱的数量: "))
#         account_money += num
#         print(f"成功存入{num}元, 账户余额{account_money}")
#     elif select == 3:
#         num = int(input("请输入取款金额: "))
#         account_money -= num
#         print(f"成功取出{num}, 账户余额{account_money}")
#     elif select == 4:
#         print("Bye")
#         break;
#     else:
#         print("你的输入有误, 请重新输入")
