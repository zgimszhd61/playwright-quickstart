# 打开文件
with open('paper.txt', 'r') as file:
    for line in file:
        print(line.strip().split(" ---- ")[1])  # 打印每行内容，并去除行尾的换行符
