"""
演示JSON数据和Python字典的相互转换
"""
import json

# 准备列表, 列表内每一个元素都是字典, 将其转换为JSON
data = [{"name": "孙悟空", "age": "500"}, {"name": "猪八戒", "age": "200"}]
json_str = json.dumps(data, ensure_ascii=False)  # ensure_ascii=False不使用ascii转换
print(type(json_str))  # <class 'str'>
print(json_str)  # [{"name": "孙悟空", "age": "500"}, {"name": "猪八戒", "age": "200"}]

# 准备字典, 将字典转换为JSON
dic = {"name": "孙悟空", "age": "500"}
json_str = json.dumps(dic)
print(type(json_str))
print(json_str)  # {"name": "\u5b59\u609f\u7a7a", "age": "500"}

# 将Json字符串转为Pyhon数据类型,字符串最外层是[]
s = '[{"name": "孙悟空", "age": "500"}, {"name": "猪八戒", "age": "200"}]'
my_list = json.loads(s)
print(type(my_list))  # <class 'list'>
print(my_list)  # [{'name': '孙悟空', 'age': '500'}, {'name': '猪八戒', 'age': '200'}]

# 将Json字符串转为Pyhon数据类型,字符串最外层是{}
s = '{"name": "\u5b59\u609f\u7a7a", "age": "500"}'
my_dic = json.loads(s)
print(type(my_dic))  # <class 'dict'>
print(my_dic)  # {'name': '孙悟空', 'age': '500'}
