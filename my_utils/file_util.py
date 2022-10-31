"""
文件处理的相关模块
"""


def print_file_info(filename):
    """
    输出指定文件的内容
    :param filename: 文件的路
    :return: None
    """
    f = None
    try:
        f = open(filename, "r", encoding="UTF-8")
        content = f.read();
        print(content)
    except Exception as e:
        print(f"程序出现异常了: {e}")
    finally:
        if f:  # 如果变量是None, 表示False, 如果与任何内容则是True
            f.close()


def append_to_file(file_name, data):
    """
    将指定的数据追加到指定的文件中国
    :param file_name: 指定的文件路径
    :param data: 指定的数据
    :return: None
    """
    f = open(file_name, "w", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()


if __name__ == "__main__":
    print_file_info("str_util.py")
    append_to_file("测试文件", "test")
