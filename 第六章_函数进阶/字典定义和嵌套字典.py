# 定义字典
my_dict1 = {}
my_dict2 = dict()

print(type(my_dict1))  # <class 'dict'>
print(type(my_dict2))  # <class 'dict'>


my_dict1 = {"HP": "惠普", "DELL": "戴尔"}

# 输出 my_dict1的内容是: {'HP': '惠普', 'DELL': '戴尔'}, 类型是: <class 'dict'>
print(f"my_dict1的内容是: {my_dict1}, 类型是: {type(my_dict1)}")

# 从字典中基于key获取value
print(my_dict1["HP"])  # 输出 惠普

# 字典的Key和Value可以是任意数据类型（Key不可为字典）
# 定义嵌套字典
computer_dict = {
    "HP": {
        "Name": "惠普",
        "CPU": "AMD",
        "Color": "silver"
    },
    "DELL": {
        "Name": "戴尔",
        "CPU": "Intel",
        "Color": "black"
    }
}

# {'HP': {'Name': '惠普', 'CPU': 'AMD', 'Color': 'silver'}, 'DELL': {'Name': '戴尔', 'CPU': 'Intel', 'Color': 'black'}}
print(computer_dict)

# 获取惠普的处理器的型号
print(computer_dict["HP"]["CPU"])  # 输出 AMD
