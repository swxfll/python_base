# 定义集合
my_set = {"Java", "Python", "Go", "Java"}
# 输出 my_set的内容是{'Go', 'Java', 'Python'}, 类型是<class 'set'>
print(f"my_set的内容是{my_set}, 类型是{type(my_set)}")

# 添加元素
my_set.add("Java")
my_set.add("Lua")
print(my_set)  # 输出 {'Lua', 'Java', 'Go', 'Python'}

# 移除元素
my_set.remove("Go")
print(my_set)  # 输出 {'Java', 'Python', 'Lua'}

# 从集合中随机删除元素
my_set.pop()
print(my_set)  # 输出 {'Lua', 'Python'}

# 清空 集合
my_set.clear()
print(my_set)  # 输出 set()

# 取出集合的差集
set1 = {1, 2, 3}
set2 = {1, 5, 6}
print(set1.difference(set2))  # 输出 {2, 3}
print(set2.difference(set1))  # 输出 {5, 6}

# 语法: 集合1.difference_update(集合2)
# 功能: 对比集合1和集合2, 在集合1内, 删除和集合2相同的元素
# 结果: 集合1被修改, 集合2不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(set1)  # 输出 {2, 3}
print(set2)  # 输出 {1, 5, 6}

# 2个集合合并
# 语法: 集合1.union(集合2)
# 功能: 将集合1和集合2组合成新集合
# 结果: 得到新结合, 集合1和集合2不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(set1)  # 输出 {1, 2, 3}
print(set2)  # 输出 {1, 5, 6}
print(set3)  # 输出 {1, 2, 3, 5, 6}

# 统计集合中的元素个数
set1 = {1, 2, 3}
print(len(set1))  # 输出 3

# 集合的遍历
set1 = {1, 2, 3}
for i in set1:
    print(i)