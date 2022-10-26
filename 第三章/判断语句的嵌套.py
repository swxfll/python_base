'''
print("欢迎来到游乐园")
if int(input("请输入你的身高:")) > 120:
    print("你的身高大于120,不可以免费")
    print("如果你的VIP等级大于3, 可以免费游玩")

    if int(input("请输入你的VIP等级: ")) > 3:
        print("恭喜你,VIP等级大于3, 可以免费游玩")
    else:
        print("Sorry, 你需要补票10元")
else:
    print("小朋友,可以免费游玩")
'''

# 1. 必须是大于等于18岁小于30岁的成年人
# 2. 同时入职时间需满足大于两年，或者级别大于3才可领取
age = 11
year = 1
level = 1
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("你的年龄达标了")
        if year > 2:
            print("恭喜你，年龄和入职时间都达标，可以领取礼物")
        elif level > 3:
            print("恭喜你，年龄和级别达标，可以领取礼物")
        else:
            print("不好意思，尽管年龄达标，但是入职时间和级别都不达标。")

    else:
        print("不好意思，年龄太大了")

else:
    print("不好意思，小朋友不可以领取。")