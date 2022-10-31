"""
字符串处理相关的模块
"""


def str_reverse(s):
    """
    将字符串进行反转
    :param s:被反转的字符串
    :return:反转后的字符串
    """
    return s[::-1]


def substr(s, x, y):
    """
    按照给定的下标完成给定字符串的切片
    :param s: 被切片的字符串
    :param x: 切片的开始下标
    :param y: 切片的结束下标
    :return: 切片完成后的字符串
    """
    return s[x:y]


if __name__ == '__main__':
    print(str_reverse("西天取经"))  # 经取天西
    print(substr("西天取经", 1, 2))  # 天
