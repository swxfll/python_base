"""
演示数据容器的通用功能
"""
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}

# len元素个数
print(f"列表 元素个数有：{len(my_list)}")  # 输出 列表 元素个数有：5
print(f"元组 元素个数有：{len(my_tuple)}")  # 输出 元组 元素个数有：5
print(f"字符串元素个数有：{len(my_str)}")  # 输出 字符串元素个数有：7
print(f"集合 元素个数有：{len(my_set)}")  # 输出 集合 元素个数有：5
print(f"字典 元素个数有：{len(my_dict)}")  # 输出 字典 元素个数有：5

# max最大元素
print(f"列表 最大的元素是：{max(my_list)}")  # 输出 列表 最大的元素是：5
print(f"元组 最大的元素是：{max(my_tuple)}")  # 输出 元组 最大的元素是：5
print(f"字符串最大的元素是：{max(my_str)}")  # 输出 字符串最大的元素是：g
print(f"集合 最大的元素是：{max(my_set)}")  # 输出 集合 最大的元素是：5
print(f"字典 最大的元素是：{max(my_dict)}")  # 输出 字典 最大的元素是：key5
# min最小元素
print(f"列表 最小的元素是：{min(my_list)}")  # 输出 列表 最小的元素是：1
print(f"元组 最小的元素是：{min(my_tuple)}")  # 输出 元组 最小的元素是：1
print(f"字符串最小的元素是：{min(my_str)}")  # 输出 字符串最小的元素是：a
print(f"集合 最小的元素是：{min(my_set)}")  # 输出 集合 最小的元素是：1
print(f"字典 最小的元素是：{min(my_dict)}")  # 输出 字典 最小的元素是：key1
# 类型转换: 容器转列表
print(f"列表转列表的结果是：{list(my_list)}")  # 输出 列表转列表的结果是：[1, 2, 3, 4, 5]
print(f"元组转列表的结果是：{list(my_tuple)}")  # 输出 元组转列表的结果是：[1, 2, 3, 4, 5]
print(f"字符串转列表结果是：{list(my_str)}")  # 输出 字符串转列表结果是：['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(f"集合转列表的结果是：{list(my_set)}")  # 输出 集合转列表的结果是：[1, 2, 3, 4, 5]
print(f"字典转列表的结果是：{list(my_dict)}")  # 输出 字典转列表的结果是：['key1', 'key2', 'key3', 'key4', 'key5']
# 类型转换: 容器转元组
print(f"列表转元组的结果是：{tuple(my_list)}")  # 输出 列表转元组的结果是：(1, 2, 3, 4, 5)
print(f"元组转元组的结果是：{tuple(my_tuple)}")  # 输出 元组转元组的结果是：(1, 2, 3, 4, 5)
print(f"字符串转元组结果是：{tuple(my_str)}")  # 输出 字符串转元组结果是：('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(f"集合转元组的结果是：{tuple(my_set)}")  # 输出 集合转元组的结果是：(1, 2, 3, 4, 5)
print(f"字典转元组的结果是：{tuple(my_dict)}")  # 输出 字典转元组的结果是：('key1', 'key2', 'key3', 'key4', 'key5')
# 类型转换: 容器转字符串
print(f"列表转字符串的结果是：{str(my_list)}")  # 输出 列表转字符串的结果是：[1, 2, 3, 4, 5]
print(f"元组转字符串的结果是：{str(my_tuple)}")  # 输出 元组转字符串的结果是：(1, 2, 3, 4, 5)
print(f"字符串转字符串结果是：{str(my_str)}")  # 输出 字符串转字符串结果是：abcdefg
print(f"集合转字符串的结果是：{str(my_set)}")  # 输出 集合转字符串的结果是：{1, 2, 3, 4, 5}
print(f"字典转字符串的结果是：{str(my_dict)}")  # 输出 字典转字符串的结果是：{'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}
# 类型转换: 容器转集合
print(f"列表转集合的结果是：{set(my_list)}")  # 输出 列表转集合的结果是：{1, 2, 3, 4, 5}
print(f"元组转集合的结果是：{set(my_tuple)}")  # 输出 元组转集合的结果是：{1, 2, 3, 4, 5}
print(f"字符串转集合结果是：{set(my_str)}")  # 输出 字符串转集合结果是：{'c', 'a', 'g', 'b', 'e', 'f', 'd'}
print(f"集合转集合的结果是：{set(my_set)}")  # 输出 集合转集合的结果是：{1, 2, 3, 4, 5}
print(f"字典转集合的结果是：{set(my_dict)}")  # 输出 字典转集合的结果是：{'key1', 'key3', 'key4', 'key2', 'key5'}
# 进行容器的排序
my_list = [3, 1, 2, 5, 4]
my_tuple = (3, 1, 2, 5, 4)
my_str = "bdcefga"
my_set = {3, 1, 2, 5, 4}
my_dict = {"key3": 1, "key1": 2, "key2": 3, "key5": 4, "key4": 5}

print(f"列表对象的排序结果：{sorted(my_list)}")  # 输出 列表对象的排序结果：[1, 2, 3, 4, 5]
print(f"元组对象的排序结果：{sorted(my_tuple)}")  # 输出 元组对象的排序结果：[1, 2, 3, 4, 5]
print(f"字符串对象的排序结果：{sorted(my_str)}")  # 输出 字符串对象的排序结果：['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(f"集合对象的排序结果：{sorted(my_set)}")  # 输出 集合对象的排序结果：[1, 2, 3, 4, 5]
print(f"字典对象的排序结果：{sorted(my_dict)}")  # 输出 字典对象的排序结果：['key1', 'key2', 'key3', 'key4', 'key5']

print(f"列表对象的反向排序结果：{sorted(my_list, reverse=True)}")  # 输出 列表对象的反向排序结果：[5, 4, 3, 2, 1]
print(f"元组对象的反向排序结果：{sorted(my_tuple, reverse=True)}")  # 输出 元组对象的反向排序结果：[5, 4, 3, 2, 1]
print(f"字符串对象反向的排序结果：{sorted(my_str, reverse=True)}")  # 输出 字符串对象反向的排序结果：['g', 'f', 'e', 'd', 'c', 'b', 'a']
print(f"集合对象的反向排序结果：{sorted(my_set, reverse=True)}")  # 输出 集合对象的反向排序结果：[5, 4, 3, 2, 1]
print(f"字典对象的反向排序结果：{sorted(my_dict, reverse=True)}")  # 输出 字典对象的反向排序结果：['key5', 'key4', 'key3', 'key2', 'key1']
