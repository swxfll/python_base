num = 0
i = 1
for i in range(1, 101):
    print(f"今天是西天取经的第{i}天,坚持")
    for j in range(1, 11):
        print(f"第{i}难, 步骤{j}")
        num += 1
    print("第 %d 难结束" % i)

print(f"第{i}天, 西天取经成功")
print(num)