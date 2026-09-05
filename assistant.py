print("你好!我是一个会算数的小助手")
name = input("你叫什么名字")
print(f"你好,{name}!我可以帮你算数")
while True:
    cmd = input("1.算数 2.打招呼 3.退出")
    if cmd == "3":
        break
    elif cmd == "2":
        print(f"你好,{name}!我可以帮你算数")
        input("请任意键继续")
    elif cmd == "1":
        try:
            a = float(input("请输入第一个数字"))
        except ValueError:
            print("你输入的不是数字")
            continue
        while True:                          # 内层小循环：专门管"问到合法运算符为止"
            op = input("请输入运算符(+-*/)")
            if op == "+" or op == "-" or op == "*" or op == "/":
                break
            print("无法运算，请重新输入")
        try:
            b = float(input("请输入第二个数字"))
        except ValueError:
            print("你输入的不是数字")
            continue
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                result = "不能除零"
            else:
                result = a / b
        else:
            result = "无法运算"
        print(result)
        input("请任意键继续")
    else:
        print("没有这个选项")
        continue