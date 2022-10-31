# 基本捕获语法
try:
    f = open("asadad", "r", encoding="UTF-8")
except:
    print("出现异常了, 将以w模式打开文件")
    f = open("asadad", "w", encoding="UTF-8")

# 捕获指定的异常
try:
    print(name)
except NameError as e:
    print('name变量名称未定义错误')

# 捕获多个异常
try:
    print(1/0)
except (NameError, ZeroDivisionError) as e:
    print("出现了变量未定义的异常")
    print(e)

# 捕获所有异常
try:
    print(1/0)
except Exception as e:
    print("出现了变量未定义的异常")
    print(e)

# 异常else
try:
    print(1)
except Exception:
    print("出现了异常")
else:
    print("好高兴, 没有异常")

# 异常的finally
try:
    print("1")
except Exception:
    print("f出现了异常")
else:
    print("f好高兴,没有异常")
finally:
    print("finally")
