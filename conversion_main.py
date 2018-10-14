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
            while True:
                conversion_tools.handle_ex_dec()
                key_str = input("输入 0 返回上级菜单，其它字符或回车继续转换：")
                if key_str == "0":
                    break
                else:
                    pass
        # 二进制转换为其它进制
        if action_str == "2":
            while True:
                conversion_tools.handle_ex_bin()
                key_str = input("输入 0 返回上级菜单，其它字符或回车继续转换：")
                if key_str == "0":
                    break
                else:
                    pass
        # 八进制转换为其它进制
        if action_str == "3":
            while True:
                conversion_tools.handle_ex_oct()
                key_str = input("输入 0 返回上级菜单，其它字符或回车继续转换：")
                if key_str == "0":
                    break
                else:
                    pass
        # 十六进制转换为其它进制
        if action_str == "4":
            while True:
                conversion_tools.handle_ex_hex()
                key_str = input("输入 0 返回上级菜单，其它字符或回车继续转换：")
                if key_str == "0":
                    break
                else:
                    pass
    # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用【进制转换工具】")
        break
    # 其他内容输入错误，需要提示用户
    else:
        print("您输入的不正确，请重新选择")
