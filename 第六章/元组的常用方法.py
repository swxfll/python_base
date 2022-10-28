t6 = ("python", "java", "lua", "python")

# 查看指定元素在元组中的下标
print(t6.index("python"))  # 输出 0

# 统计指定元素在元组中个个数
print(t6.count('python'))  # 输出 2

# 统计元组中元素的个数
print(len(t6))  # 输出 4

# 元组内的元素不可以修改, 但如果元组中的元素是列表时, 可以修改列表里面的元素
t9 = (1, 2, ["java", "lua"])
t9[2][0] = "python"
print(t9)  # 输出 (1, 2, ['python', 'lua'])
