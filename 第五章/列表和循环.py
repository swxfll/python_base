num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_list2 = list()
num_list3 = []
i = 0
while i < len(num_list):
    if num_list[i] % 3 == 0:
        num_list2.append(num_list[i])
    i += 1

print("-------------------------")

for i in num_list:
    if i % 6 == 0:
        num_list3.append(i)

print(num_list2)
print(num_list3)
