mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

temp_list = []

index = 0
while index < len(mylist):
    if mylist[index] % 2 == 0:
        temp_list.append(mylist[index])
    index += 1

print(temp_list)

temp_list2 = []
for i in mylist:
    if i % 2 == 0:
        temp_list2.append(i)

print(temp_list2)
