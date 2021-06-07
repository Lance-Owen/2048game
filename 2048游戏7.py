#上下左右四个方向的数据变化
import numpy as np

def go_up():
    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("初始矩阵\n", np.array(a))
    global a                        #设为全局变量，实现不同按钮之间可以循环使用a
    b=[]
    for i in range(0,4):
        b.append([])
        for j in range(0,4):
            b[i].append(a[j][i])
    a = []
    for i in range(0, 4):
        a.append([])
        for j in range(0, 4):
            a[i].append(b[j][i])
    return a
    # print("向上累加前转化为\n",np.array(b))
    # print("输出矩阵\n",np.array(a))
def go_down():
    global a
    b=[]
    for i in range(0,4):
        b.append([])
        for j in range(3,-1,-1):
            b[i].append(a[j][i])
    a = []
    i = 0
    for j in range(3, -1, -1):
        a.append([])
        for k in range(0, 4):
            a[i].append(b[k][j])
        i = i + 1
    print("向下累加前转化为\n",np.array(b))
    print("输出矩阵\n",np.array(a))
def go_right():
    global a
    b=[]
    for i in range(0,4):
        b.append([])
        for j in range(3,-1,-1):
            b[i].append(a[i][j])
    a = []
    for i in range(0, 4):
        a.append([])
        for j in range(3, -1, -1):
            a[i].append(b[i][j])
    print("向右累加前转化为\n",np.array(b))
    print("输出矩阵\n",np.array(a))

# c=go_up()
# print(c)
go_down()
# go_right()


