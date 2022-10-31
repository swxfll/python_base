str = "itheima itcast boxuegu"
print("it字符一共有: %d 个" % str.count("it"))
print("将字符串内的空格，全部替换为字符：'|': %s", str.replace(" ", "|"))
print("并按照'|'进行字符串分割，得到列表: %s" % str.replace(' ', '|').split('|'))