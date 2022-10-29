# 打开文件
import time

f = open("D:/test.txt", "r", encoding="UTF-8")
print(type(f))  # <class '_io.TextIOWrapper'>

# 读取文件
# print(f"读取10个字节的结果:\n{f.read(10)}")
# print(f"read方法读取全部内容的结果是:\n{f.read()}")

# 读取文件 - readline()
# 读取文件的全部行, 封装到列表中
# lines = f.readlines()
# print(type(lines))
# print(lines)

# readline()
# 一次读取一行
#line1 = f.readline()
#print(line1)

# for循环读取文件行
for line in open("D:/test.txt", "r", encoding="UTF-8"):
    print(line, end='')

# 睡眠
#time.sleep(5000000)

# 文件的关闭
#f.close()

# with open 实现自动关闭文件
with open("D:/test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行的数据是: {line}")

time.sleep(5000000)