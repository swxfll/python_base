import random

money = 10000
for i in range(1, 21):
    score = random.randint(1, 10)

    if score < 5:
        print(f"员工{i}绩效{score}, 不满足, 不发工资, 下一位")
        continue

    # 要判断余额足不足
    if money >= 1000:
        money -= 1000
        print(f"员工{i}, 满足条件发工资1000,公司账户余额: {money}")
    else:
        print(f"余额不足, 当前余额{money}, 不足以发工资, 不发了")
        break