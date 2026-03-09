import os

def check_disk():
    output = os.popen("df / | tail -1").read()
    usage = int(output.split()[4].replace("%", ""))
    print(f"磁盘使用率：{usage}%")
    if usage > 80:
        print("⚠️  警告：磁盘使用率过高！")
    elif usage > 60:
        print("📊 注意：磁盘使用率较高")
    else:
        print("✅ 磁盘状态正常")

def check_memory():
    output = os.popen("free -h | grep 内存").read()
    parts = output.split()
    print(f"内存总量：{parts[1]}  已用：{parts[2]}  可用：{parts[3]}")

def check_cpu():
    output = os.popen("top -bn1 | grep 'Cpu'").read()
    print(f"CPU状态：{output.strip()}")

print("===== 系统巡检报告 =====")
check_disk()
check_memory()
check_cpu()
print("========================")
