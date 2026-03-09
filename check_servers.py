import os

output = os.popen("df / | tail -1 |awk '{print $5}'").read()
usage = int(output.strip().replace("%",""))

print(f"当前磁盘使用率:{usage}%")

if usage > 80:
	print("⚠️  警告：磁盘使用率过高！")
elif usage > 60:
        print("📊 注意：磁盘使用率较高")
else:
        print("✅ 磁盘状态正常")
