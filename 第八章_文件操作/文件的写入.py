import time

# 以w模式打开文件, 文件不存在, 会创建文件
# 以w模式打开文件, 文件存在, 会清空原有内容并写入新的内容
f = open("ll.txt", "w", encoding="UTF-8")

# write写入
f.write("Hello World")

# 手动刷新
#f.flush()  # 将内存中积攒的内容, 写入到硬盘文件中
f.close()  # close方法, 内置了flush的功能

