#1.   数字随机产生，范围1-10
#2.   有3次机会猜测数字，通过3层嵌套判断实现
#3.   每次猜不中，会提示大了或小了

import random
num = random.randint(1, 10)

guess_num = int(input("请输入你要猜的数字: "))

if guess_num == num:
    print("恭喜你,第一次就猜中了")
else:
    if guess_num > num:
        print("你猜的数字大了")
    else:
        print("你猜的数字小了")

    guess_num = int(input("请输入你要猜的数字: "))

    if guess_num == num:
        print("恭喜你, 第二次就猜中了")
    else:
        if guess_num > num:
            print("你猜的数字大了")
        else:
            print("你猜的数字小了")

        guess_num = int(input("请输入你要猜的数字: "))

        if guess_num == num:
            print("恭喜你, 第三次就猜中了")
        else:
            print("抱歉, 你没机会了")