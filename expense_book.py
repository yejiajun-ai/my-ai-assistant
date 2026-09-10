import json
from datetime import datetime
bills = []
try:
    with open("bills.txt", "r", encoding="utf-8") as f:
        for line in f.read().splitlines():
            bills.append(json.loads(line))
except FileNotFoundError:
    bills = []


def 显示列表(bills):
    """打印消费明细，带编号。"""
    n = 0
    for item in bills:
        n = n + 1
        print(f"{n}. [{item['时间']}] {item['项目']} {item['金额']:.2f} 元（{item['分类']}）")
    print("=" * 30)


print()
print("===== 个人记账本 v1 =====")

while True:
    cmd = input("1.记一笔  2.查看全部  3.删一笔  4.改一笔  5.统计  6.退出")

    if cmd == "6":
        print("再见！")
        break
    elif cmd == "1":
        项目名 = input("消费项目")
        while True:
            try:
                金额 = float(input("金额"))
                break
            except ValueError:
                print("请输入数字")
                continue
        分类 = input("分类")
        时间 = datetime.now().strftime("%m-%d %H:%M")
        record = {"时间": 时间, "项目": 项目名, "金额": 金额, "分类": 分类}
        bills.append(record)
        with open("bills.txt", "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(f"已记录：[{时间}] {项目名}  {金额:.2f} 元（{分类}）")
    elif cmd == "2":
        if len(bills) == 0:
            print("还没有记录")
        else:
            print("===== 当前记录 =====")
            显示列表(bills)
            print(f"共 {len(bills)} 条记录")
        input("按任意键返回菜单")
    elif cmd == "3":
        if len(bills) == 0:
            print("没有记录可以删除")
            input("请按任意键返回")
            continue
        print("===== 当前记录 =====")
        显示列表(bills)
        while True:
            s = input("请选择你需要删除的记录编号,返回请输入q")
            if s == "q":
                break
            try:
                m = int(s)
            except ValueError:
                print("请输入数字")
                continue
            if 1 <= m <= len(bills):
                deleted = bills.pop(m - 1)
                print(f"已删除：[{deleted['时间']}] {deleted['项目']} {deleted['金额']:.2f} 元")
                with open("bills.txt", "w", encoding="utf-8") as f:
                    for b in bills:
                        f.write(json.dumps(b, ensure_ascii=False) + "\n")
                print(f"还剩 {len(bills)} 条记录")
                break
            else:
                print(f"编号不存在，请输入1~{len(bills)}之间的数字")
                continue
        input("按任意键返回菜单")
    elif cmd == "4":
        if len(bills) == 0:
            print("没有记录可以修改")
            input("请按任意键返回")
            continue
        print("===== 当前记录 =====")
        显示列表(bills)
        while True:
            s = input("请选择你需要修改的记录编号,返回请输入q")
            if s == "q":
                break
            try:
                m = int(s)
            except ValueError:
                print("请输入数字")
                continue
            if 1 <= m <= len(bills):
                bill = bills[m - 1]
                print(f"当前：[{bill['时间']}] {bill['项目']} {bill['金额']:.2f} 元（{bill['分类']}）")
                新项目 = input(f"消费项目（直接回车保持原值：{bill['项目']}）")
                if 新项目:
                    bill["项目"] = 新项目
                新分类 = input(f"分类（直接回车保持原值：{bill['分类']}）")
                if 新分类:
                    bill["分类"] = 新分类
                while True:
                    新金额 = input(f"金额（直接回车保持原值：{bill['金额']}）")
                    if 新金额 == "":
                        break
                    try:
                        bill["金额"] = float(新金额)
                        break
                    except ValueError:
                        print("请输入数字")
                        continue
                with open("bills.txt", "w", encoding="utf-8") as f:
                    for b in bills:
                        f.write(json.dumps(b, ensure_ascii=False) + "\n")
                print(f"已修改：[{bill['时间']}] {bill['项目']} {bill['金额']:.2f} 元（{bill['分类']}）")
                break
            else:
                print(f"编号不存在，请输入1~{len(bills)}之间的数字")
                continue
        input("按任意键返回菜单")
    elif cmd == "5":
        if len(bills) == 0:
            print("还没有记录")
            input("按任意键返回菜单")
            continue
        total = 0
        for bill in bills:
            total = total + bill["金额"]
        print("===== 消费统计 =====")
        print(f"总笔数：{len(bills)}")
        print(f"总金额：{total:.2f} 元")
        print("-" * 30)
        # 按分类统计
        分类统计 = {}
        for bill in bills:
            c = bill["分类"]
            if c not in 分类统计:
                分类统计[c] = 0
            分类统计[c] = 分类统计[c] + bill["金额"]
        print("按分类：")
        for c, amt in 分类统计.items():
            print(f"  {c}：{amt:.2f} 元")
        print("=" * 30)
        input("按任意键返回菜单")
    else:
        print("没有这个选项")
