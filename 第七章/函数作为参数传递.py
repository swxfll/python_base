# 定义一个函数, 接收另一个函数作为传入参数
# test_func需要一个函数作为参数传入，这个函数需要接收2个数字进行计算，计算逻辑由这个被传入函数决定
def test_func(compute):
    result = compute(1, 2)  # 确定compute是函数
    print(type(compute))  # <class 'function'>
    print(f"计算结果是: {result}")  # 计算结果是: 3

#compute函数接收2个数字对其进行计算，compute函数作为参数，传递给了test_func函数使用
def compute(x, y):
    return x + y

# 函数compute，作为参数，传入了test_func函数中使用。
# 最终，在test_func函数内部，由传入的compute函数，完成了对数字的计算操作
# 这是一种，计算逻辑的传递，而非数据的传递。
test_func(compute)