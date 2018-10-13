#! /usr/bin/python3

import conversion_tools
# 无限循环，由用户主动决定什么时候退出循环！
while True:

    #  显示功能菜单
    conversion_tools.show_menu()

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)

    # 1,2,3,4 针对工具的操作
    if action_str in ["1", "2", "3", "4"]:

        # 十进制转换为其它进制
        if action_str == "1":
            conversion_tools.dec_to_others()
        # 二进制转换为其它进制
        if action_str == "2":
            conversion_tools.bin_to_others()
        # 八进制转换为其它进制
        if action_str == "3":
            conversion_tools.oct_to_others()
        # 十六进制转换为其它进制
        if action_str == "4":
            conversion_tools.hex_to_others()
    # 0 退出系统
    elif action_str == "0":

        print("欢迎再次使用【进制转换工具】")

        break
        # pass
    # 其他内容输入错误，需要提示用户
    else:
        print("您输入的不正确，请重新选择")
