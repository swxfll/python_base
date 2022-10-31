my_dict1 = {"HP": "惠普", "DELL": "戴尔"}

# 新增元素
my_dict1["APPLE"] = "橘子"

# 更新元素
# 字典Key不可以重复，所以对已存在的Key执行上述操作，就是更新Value值
my_dict1["APPLE"] = "苹果"

# 删除元素
my_dict1.pop("APPLE")
print(my_dict1)  # 输出 {'HP': '惠普', 'DELL': '戴尔', 'APPLE': '苹果'}

# 清空元素
my_dict1.clear()
print(my_dict1)  # 输出 {}

# 获取字典中的所有key
my_dict1 = {"HP": "惠普", "DELL": "戴尔"}
print(my_dict1.keys())  # 输出 dict_keys(['HP', 'DELL'])
# 遍历字典
# 方式1: 通过获取全部的key来完成遍历
for key in my_dict1.keys():
    print(f"字典的key是: {key}")
    print(f"字典的value是: {my_dict1[key]}")

# 方式2: 直接对字典进行for循环, 每一次循环都是直接得到key, 和方式1的输出结果是一致的
for key in my_dict1:
    print(f"字典的key是: {key}")
    print(f"字典的value是: {my_dict1[key]}")

# 统计字典额元素数量
print(len(my_dict1))  # 输出 2
