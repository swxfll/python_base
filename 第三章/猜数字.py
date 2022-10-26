num = 10
if int(input("请输入数字")) == num:
    print("恭喜你,猜对了")
elif int(input("不对,再猜一次")) == num:
    print("恭喜你,猜对了")
elif int(input("不对,在猜最后一次:")) == num:
    print("恭喜你,猜对了")
else:
    print("Sorry,全部猜错了,数字是: %d" % num)