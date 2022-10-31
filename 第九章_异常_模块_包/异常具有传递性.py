# 定义一个出现异常的方法
def fun1():
    print("fun1 开始执行")
    num = 1 / 0
    print("fun1 执行结束")


# 定义一个无异常的方法,调用fun1
def fun2():
    print("fun2开始执行")
    fun1()
    print("fun2执行结束")


# 定义一个方法, 调用上面的方法
def main():
    fun2()


main()
