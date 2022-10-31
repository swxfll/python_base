# 局部变量
def test_fun():
    num = 100
    print(num)


test_fun()
#print(num) # 报错:NameError: name 'num' is not defined

# 全局变量
# num2 = 200
#
#
# def test_a():
#     print(f"test_a: {num2}")
#
#
# def test_b():
#     print(f"test_a: {num2}")


# test_a()
# test_b()

# 设置内部定义的变量为全局变量
num3 = 200


def test_d():
    global num3
    num3 = 500


test_d()
print(num3)


