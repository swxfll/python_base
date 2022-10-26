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