"""
统计文件中指定字符出现的次数
itheima itcast python
itheima python itcast
beijing shanghai itheima
shenzhen guangzhou itheima
wuhan hangzhou itheima
zhengzhou bigdata itheima
"""

f = open("word.txt", "r", encoding="UTF-8")

# 方式1, read() 读取全部内容, 通过字符串的count方法统计单词数量
#content = f.read()
#print(content.count("itheima"))

# 方式2: 使用for方式一行一行读取
count = 0
for line in f:
    # 使用strip()去除开头和结尾的空格以及换行符
    # 使用split(" ")将字符串以空格分割转为列表
    line = line.strip().split(" ")

    for word in line:
        if word == "itheima":
            count += 1
print(count)

