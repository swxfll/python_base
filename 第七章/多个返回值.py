def test_return():
    return 1, "hello", True


x, y, z = test_return()
print(x)  # 输出 1
print(y)  # 输出 hello
print(z)  # 输出 True
