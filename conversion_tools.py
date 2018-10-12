

def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用【进制转换工具】V 1.0")
    print("")
    print("1. 十进制转换为其它进制")
    print("2. 二进制转换为其它进制")
    print("3. 八进制转换为其它进制")
    print("4. 十六进制转换为其它进制")
    print("")
    print("0. 退出系统")
    print("*" * 50)


# 十进制转换
def ten_to_others():
    # 获取用户输入十进制数
    ten = int(input("请输入十进制数字："))

    print("十进制数为：", ten)

    # 转换为二进制数
    two = bin(ten)

    print("转换为二进制为：", two[2:])

    # 转换为八进制数
    eight = oct(ten)

    print("转换为八进制为：", eight[2:])

    # 转换为十六进制数
    sixteen = hex(ten)

    print("转换为十六进制为：", sixteen[2:])


# 八进制转换
def eight_to_others():
    # 获取用户输入八进制数
    eight = (input("请输入八进制数字："))
    print("八进制数为：", eight)

    # 将八进制数转换成十进制数
    eight = int(eight, 8)

    # 转换为二进制数
    two = bin(eight)

    print("转换为二进制为：", two[2:])

    # 转换为十进制数
    ten = int(eight)

    print("转换为十进制为：", ten)

    # 转换为十六进制数
    sixteen = hex(eight)

    print("转换为十六进制为：", sixteen[2:])


# 二进制转换
def two_to_others():
    # 1.准备工作
    # 获取用户输入二进制数
    two = (input("请输入二进制数字："))
    print("二进制数为：", two)

    # 将二进制数转换成十进制数
    two = int(two, 2)

    # 2.开始转换
    # 转换为八进制数
    twice = oct(two)

    print("转换为八进制为：", twice[2:])

    # 转换为十进制数
    ten = int(two)

    print("转换为十进制为：", ten)

    # 转换为十六进制数
    sixteen = hex(two)

    print("转换为十六进制为：", sixteen[2:])


# 八进制转换
def sixteen_to_others():
    # 获取用户输入十六进制数
    sixteen = (input("请输入十六进制数字："))
    print("十六进制数为：", sixteen)

    # 将十六进制数转换成十进制数
    sixteen = int(sixteen, 16)

    # 转换为二进制数
    two = bin(sixteen)

    print("转换为二进制为：", two[2:])

    # 转换为八进制数
    eight = oct(sixteen)

    print("转换为八进制为：", eight[2:])

    # 转换为十进制数
    ten = int(sixteen)

    print("转换为十进制为：", ten)
