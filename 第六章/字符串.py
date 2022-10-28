my_str = "Java And Python"

# 通过下标获取值
print(my_str[0])  # 输出 J
print(my_str[-1])  # 输出 n

# 同元组一样, 字符串中的元素是不可以修改的
# my_str[0] = 'A'  # 报错 TypeError: 'str' object does not support item assignment

my_str = "Java And Python"

# index
print(my_str.index("a"))  # 输出 1

# replace 字符串的替换
# replace不是修改字符串本身, 而是返回一个被修改后的新的字符串
print(my_str.replace('Java', 'Lua'))  # 输出 Lua And Python

# split
# 字符串本身不变, 而是得到一个列表对象
print(my_str.split(" "))  # 输出 ['Java', 'And', 'Python']

# 字符串的规整操作(去除前后空格)
my_str = "   Java And Python   "
print(my_str.strip())

# 字符串的规整操作(去除前后指定的字符串)
my_str = "12Python21"
print(my_str.strip("12"))  # 输出 Python

# count
# 统计字符串中某字符出现的次数
my_str = "12Python21"
print(my_str.count('1'))  # 输出 2

# len
# 统计字符串的长度
my_str = "123456"
print(len(my_str))  # 输出 6
