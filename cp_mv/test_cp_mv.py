import os

source = os.path.join(os.path.dirname(__file__), 'source')
target = os.path.join(os.path.dirname(__file__), 'target')

if os.path.exists(target):
    os.system(f"rm -rf {target}")
os.makedirs(target)

if os.path.exists(source):
    os.system(f"rm -rf {source}")
os.makedirs(source)
os.system(f"touch {source}/temp.txt")

# 把source下的所有文件拷贝到target下
# 以下2条命令等价
cmd1 = f"cp {source}/* {target}/"
cmd1 = f"cp -r {source}/* {target}"

# 把source文件夹拷贝到target下
# 以下4条命令等价
cmd1 = f"cp -r {source}/ {target}/"
cmd1 = f"cp -r {source} {target}/"
cmd1 = f"cp -r {source}/ {target}"
cmd1 = f"cp -r {source} {target}"

# 把source文件夹移动到target下
# 以下2条命令等价
cmd1 = f"mv {source}/* {target}/"
cmd1 = f"mv {source}/* {target}"

# 把source文件夹移动到target下
# 以下4条命令等价
cmd1 = f"mv {source}/ {target}/"
cmd1 = f"mv {source} {target}/"
cmd1 = f"mv {source}/ {target}"
cmd1 = f"mv {source} {target}"

os.system(cmd1)