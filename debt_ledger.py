import json

# 启动时从文件读回记录
# 文件里每行是一段 JSON 文字，json.loads 能把它变回字典
try:
    with open("debt.txt", "r", encoding="utf-8") as f:
        debt = []
        for line in f.read().splitlines():
            try:
                record = json.loads(line)
                if isinstance(record, dict):    # 只要字典，别的行跳过
                    debt.append(record)
            except ValueError:
                continue    # 旧格式（如 "张三|500"）或坏行 → 跳过
except FileNotFoundError:
    debt = []

print("===== 欠款台账 v2（字典版） =====")
while True:
    cmd=input("1.添加客户  2.查看全部  3.删除一条  4.清空全部  5.统计  6.退出")
    if cmd == "6":
        break
    elif cmd == "5":
        total = 0
        for c in debt:
            total = total + c["欠款"]       # 直接喊键名，不用 split 不用 float
        print("===== 欠款统计 =====")
        print(f"欠款总额：{total}")
        print(f"客户数量：{len(debt)}")
        print("=" * 30)
        input("按任意键返回菜单")
    elif cmd == "4":
        if len(debt) == 0:
            print("还没有记录")
        else:
            confirm = input(f"确定要清空全部 {len(debt)} 条记录吗？(y/n)")
            if confirm == "y":
                debt.clear()
                open("debt.txt", "w").close()
                print("已清空记录")
            else:
                print("已取消")
        input("按任意键返回菜单")
    elif cmd == "3":
        if len(debt) == 0:
            print("还没有记录")
            input("按任意键返回菜单")
            continue
        while True:
            n = input("请输入要删除的客户编号（输入q返回菜单）")
            if n == "q":
                break
            try:
                m = int(n)
            except ValueError:
                print("请输入数字")
                continue
            if 1 <= m <= len(debt):
                deleted = debt.pop(m - 1)
                print(f"已删除：{deleted['姓名']} 欠 {deleted['欠款']} 元")
                print(f"还剩 {len(debt)} 条")
                with open("debt.txt", "w", encoding="utf-8") as f:
                    for c in debt:
                        # ensure_ascii=False 让中文原样存，不然会变成 \u5f20 这种
                        f.write(json.dumps(c, ensure_ascii=False) + "\n")
                break
            else:
                print(f"编号不存在，请输入1~{len(debt)}之间的数字")
                continue
        input("按任意键返回菜单")
    elif cmd == "2":
        if len(debt) == 0:
            print("还没有客户记录")
        else:
            print(f"===== 欠款列表（共 {len(debt)} 条）=====")
            n = 0
            for c in debt:
                n = n + 1
                # 想怎么显示就怎么拼，数据本身不再带格式
                print(f"第{n}条：{c['姓名']} 欠 {c['欠款']} 元")
            print("=" * 30)
            print(f"共 {len(debt)} 条记录")
        input("按任意键返回菜单")
    elif cmd == "1":
        name = input("请输入客户姓名")
        while True:
            amount_input = input("请输入欠款金额")
            try:
                amount = float(amount_input)
                break
            except ValueError:
                print("请输入数字")
                continue
        record = {"姓名": name, "欠款": amount}    # 一条记录就是一个字典
        debt.append(record)
        with open("debt.txt", "a", encoding="utf-8") as f:
            # 字典不能直接 write，先用 json.dumps 变成一段文字
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
        print(f"已添加：{record['姓名']} 欠 {record['欠款']} 元")
        input("按任意键返回菜单")
    else:
        print("没有这个选项")
        input("按任意键返回菜单")
