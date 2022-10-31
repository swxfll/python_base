"""
演示异常,模块,包的综合案例
"""
import datetime

# 创建my_utils包,在包内创建: str_util.py和file_util模块

import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("西天取经"))  # 经取天西
print(my_utils.str_util.substr("012345", 0, 2))  # 01

file_util.append_to_file("test.txt", "data")
file_util.print_file_info("test.txt")
