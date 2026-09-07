try:
    with open("history.txt", "r", encoding="utf-8") as f:
        history = f.read().splitlines()
except FileNotFoundError:
    history = []        
name=input("你好,我叫算数小能手,你叫什么名字")
input(f"你好,{name},请输入任意键进入菜单")
while True:
    cmd=input("1.算数,2.打招呼,3.历史,4.退出")
    if cmd == "1":
        try:
            a=float(input("请输入你需要计算的第一个数字"))
        except ValueError:
            print("请输入数字进行计算")
            input("按任意键返回菜单")
            continue
        while True:
            op=input("请输入运算符(+-*/)")
            if op in ("+", "-", "*", "/"):
                break
            print("运算符有误,请重新输入")
        try:
            b = float(input("请输入你需要计算的第二个数字"))
        except ValueError:
            print("请输入数字进行计算")
            input("按任意键返回菜单")
            continue
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            if b == 0:
                print("无法除零")
                input("按任意键返回菜单")
                continue
            result = a / b
        print(result)
        record = f"{a} {op} {b} = {result}"
        history.append(record)
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(record + "\n")
        input("按任意键返回菜单")
    elif cmd == "2":
        print(f"你好,{name}!我是你的计算小助手")
        input("按任意键返回菜单")
    elif cmd == "3":
        if len(history) == 0:
            print("还没有计算记录")
        else:
            n = 0
            for item in history:
                n = n + 1
                print(f"第{n}题：{item}")
            print(f"共 {len(history)} 条记录")
        input("按任意键返回菜单")
    elif cmd == "4":
        break
    else:
        print("没有这个选项")
        input("按任意键返回菜单")
