import os

totalSize = 0
fileNum = 0
dirNum = 0


def visitDir(path):
    global totalSize
    global fileNum
    global dirNum
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        #print(sub_path)
        if os.path.isfile(sub_path):
            fileNum = fileNum+1                      # 统计文件数量
            totalSize = totalSize+os.path.getsize(sub_path)  # 文件总大小
        elif os.path.isdir(sub_path):
            dirNum = dirNum+1                       # 统计文件夹数量
            visitDir(sub_path)                           # 递归遍历子文件夹