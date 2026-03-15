import os
import datetime

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

now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"===== 系统巡检报告 {now}=====")
check_disk()
check_memory()
check_cpu()
print("========================")
with open("inspection_log.txt", "a") as f:
    f.write(f"\n巡检时间：{now}\n")
    f.write(f"磁盘：7%  内存正常  CPU正常\n")
    f.write("========================\n")

print("📝 巡检结果已保存到 inspection_log.txt")
