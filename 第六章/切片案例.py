# 获取my_str中的黑马程序员
my_str = "万过薪月，员序程马黑来，nohtyP学"
my_str = my_str[::-1].split("，")[1].replace("来", "")
my_str = my_str.split("，")[1][::-1].strip("来")
my_str = my_str[::-1][9:14]
my_str = my_str[5:10][::-1]