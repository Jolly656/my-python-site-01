import os
import shutil

# 定义源文件夹（Obsidian Vault）
source = r"D:\Zhuomian\my-python-site-01\content\my-python-site-01"

# 定义目标文件夹（Quartz content）
target = r"D:\Zhuomian\my-python-site-01\content"

# 遍历源文件夹
for root, dirs, files in os.walk(source):
    for file in files:
        if file.endswith(".md"):
            src_file = os.path.join(root, file)
            dst_file = os.path.join(target, file)
            shutil.copy2(src_file, dst_file)

print("✅ 笔记复制完成！")
