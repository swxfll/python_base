mylist = ["java", "python", "lua"]

# 查找元素在列表的下表索引
print(mylist.index("lua"))  # 输出 2

# 待查找的元素不存在,会报错
# print(mylist.index("hello"))

# 修改列表中元素的值
mylist[0] = 'go'
print(mylist)  # 输出 ['go', 'python', 'lua']

# 在指下标位置插入新的元素
mylist.insert(1, "html")
print(mylist)  # 输出 ['go', 'html', 'python', 'lua']

# 在列表的尾部追加元素
mylist.append("end")
print(mylist)  # 输出 ['go', 'html', 'python', 'lua', 'end']

# 在列表的尾部追加多个元素
mylist.extend([1, 2])
print(mylist)  # 输出 ['go', 'html', 'python', 'lua', 'end', 1, 2]

mylist = ["java", "python", "lua"]
# 删除指定指定下标的元素1
del mylist[0]
print(mylist)  # 输出 ['python', 'lua']

# 删除指定指定下标的元素2
# pop会删除元素, 并返回删除的元素
mylist.pop(-1)
print(mylist)  # 输出 ['python']

mylist = ["java", "python", "java"]
# 删除指定元素在列表中的第一个匹配项
mylist.remove("java")
print(mylist)  # 输出 ['python', 'java']

# 统计指定元素在列表中的数量
count = mylist.count("python")
print(count)  # 输出 1

# 统计列表中元素的数量
print(len(mylist))  # 输出 2

# 清空列表
mylist.clear()
print(mylist)  # 输出 []


