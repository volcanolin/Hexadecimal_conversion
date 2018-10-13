

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
def dec_to_others():
    # 1.准备工作
    # 获取用户输入的十进制数
    dec_num = int(input("请输入十进制数字："))
    print("十进制数为：", dec_num)

    # 2.开始转换
    # 转换为二进制数
    bin_num = bin(dec_num)
    print("转换为二进制为：", bin_num[2:])

    # 转换为八进制数
    oct_num = oct(dec_num)
    print("转换为八进制为：", oct_num[2:])

    # 转换为十六进制数
    hex_num = hex(dec_num)
    print("转换为十六进制为：", hex_num[2:])


# 二进制转换
def bin_to_others():
    # 1.准备工作
    # 获取用户输入的二进制数
    bin_num = (input("请输入二进制数字："))
    print("二进制数为：", bin_num)

    # 将二进制数转换成十进制数
    bin_num = int(bin_num, 2)

    # 2.开始转换
    # 转换为八进制数
    oct_num = oct(bin_num)
    print("转换为八进制为：", oct_num[2:])

    # 转换为十进制数
    dec_num = int(bin_num)
    print("转换为十进制为：", dec_num)

    # 转换为十六进制数
    hex_num = hex(bin_num)
    print("转换为十六进制为：", hex_num[2:])


# 八进制转换
def oct_to_others():
    # 1.准备工作
    # 获取用户输入的八进制数
    oct_num = (input("请输入八进制数字："))
    print("八进制数为：", oct_num)

    # 将八进制数转换成十进制数
    oct_num = int(oct_num, 8)

    # 2.开始转换
    # 转换为二进制数
    bin_num = bin(oct_num)
    print("转换为二进制为：", bin_num[2:])

    # 转换为十进制数
    dec_num = int(oct_num)
    print("转换为十进制为：", dec_num)

    # 转换为十六进制数
    hex_num = hex(oct_num)
    print("转换为十六进制为：", hex_num[2:])


# 十六进制转换
def hex_to_others():
    # 1.准备工作
    # 获取用户输入的十六进制数
    hex_num = (input("请输入十六进制数字："))
    print("十六进制数为：", hex_num)

    # 将十六进制数转换成十进制数
    hex_num = int(hex_num, 16)

    # 2.开始转换
    # 转换为二进制数
    bin_num = bin(hex_num)
    print("转换为二进制为：", bin_num[2:])

    # 转换为八进制数
    oct_num = oct(hex_num)
    print("转换为八进制为：", oct_num[2:])

    # 转换为十进制数
    dec_num = int(hex_num)
    print("转换为十进制为：", dec_num)
