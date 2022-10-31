# 导入自定义模块使用
# import my_module
# my_module.test(1, 2)
#
# from my_module import test
# test(1, 2)

# 导入不同模块的同名功能
# from my_module import test
# from my_module2 import test
#
# test(1, 2)  # -1

# __main__
# from my_module import test
# test(1, 2)

# __all__
# 不能调用test_B(), 以import all_module方式导入则不受影响
from all_module import *
test_A()



