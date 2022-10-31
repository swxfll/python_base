my_list = [0, 1, 2, 3, 4, 5, 6]
result = my_list[1:4]  # 步长默认是1, 可以省略不写
print(result)  # 输出 [1, 2, 3]

my_tuple = (0, 1, 2, 3, 4, 5, 6)
result = my_tuple[:]  # 起始和结束不写表示从头到尾,步长为1可以省略
print(result)  # 输出 (0, 1, 2, 3, 4, 5, 6)

my_str = "01234567"
result = my_str[::2]  # 对my_str进行切片, 从头到尾, 步长为2
print(result)  # 输出 0246

my_str = "01234567"
result = my_str[::-1]  # 对my_str进行切片, 从头到尾, 步长为-1, 等同于将序列翻转
print(result)  # 输出 76543210

my_list = [0, 1, 2, 3, 4, 5, 6]
result = my_list[3:1:-1]  # 对my_list列表进行操作, 从3开始到1结束, 步长为-1
print(result)  # 输出 [3, 2]

my_tuple = (0, 1, 2, 3, 4, 5, 6)
result = my_tuple[::-2]  # 对元组进行切片, 从头到尾, 步长-2
print(result)  # 输出 (6, 4, 2, 0)