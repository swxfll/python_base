name = input("前输入")
print("你输入的是: %s" % name)

# 输入数字类型, input默认接收的都是字符串
num = input("请告诉我你的银行卡密码")
num = int(num)
print("你的银行卡密码类型是: ", type(num))

# 输出
'''
前输入123
你输入的是: 123
请告诉我你的银行卡密码123
你的银行卡密码类型是:  <class 'int'>
'''