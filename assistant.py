# 启动时读取历史文件（文件不存在则从空列表开始）
history = []
try:
    with open("history.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                history.append(line)
except FileNotFoundError:
    pass

name = input("你好,你叫什么名字,我是你的计算小助手")
input(f"你好,{name},请按任意键进入菜单")
while True:
    cmd = input("1.开始算数,2.打招呼,3.查看历史,4.退出")
    if cmd == "4":
        break
    elif cmd == "3":
        if len(history) == 0:
            print("还没有计算记录")
        else:
            print(f"===== 计算历史（共 {len(history)} 条）=====")
            for i, item in enumerate(history, start=1):
                print(f"{i}. {item}")
        input("按任意键返回菜单")
    elif cmd == "2":
        print(f"你好,{name}!我是你的计算小助手")
        input("按任意键返回菜单")
    elif cmd == "1":
        try:
            a = float(input("请输入第一个数字"))
        except ValueError:
            print("你输入的不是数字")
            input("按任意键返回菜单")
            continue
        while True:
            op = input("请输入运算符(+-*/)")
            if op in ("+", "-", "*", "/"):
                break
            print("运算符有误,请重新输入")
        try:
            b = float(input("请输入第二个数字"))
        except ValueError:
            print("你输入的不是数字")
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
        # 追加写入文件，重启后记录还在
        with open("history.txt", "a", encoding="utf-8") as f:
            f.write(record + "\n")
        input("按任意键返回菜单")
    else:
        print("没有这个选项")
        input("按任意键返回菜单")
