"""
while猜数字案例
"""

import random
num = random.randint(1, 100)

# 定义变量总共猜了多少次
count = 0

while True:
    guess_num = int(input("请输入你要猜的数字: "))
    count += 1
    if num == guess_num:
        print("恭喜你, 猜对了, 一共猜了 %d 次" % count)
        break
    else:
        if num < guess_num:
            print("猜的数字过大")
        else:
            print("猜的数字过小")