import tkinter as tk
import numpy as np      #打印矩阵便于分析
import random           #随机函数
win = tk.Tk()            # 创建窗口
win.title("2048小游戏")  # 窗口名称
win.geometry("410x600")  # 窗口的大小
win.resizable(width=True, height=True)  # 窗口大小可变，True可变
# 创建画布
canvas = tk.Canvas(win, width=410, height=410, bg="tan")    #画布
num_color = ['burlywood', 'oldlace', 'moccasin', 'orange', 'coral', 'tomato', 'orangered', 'khaki', 'gold',
             'goldenrod', 'lightgreen', 'limegreen']        #每一个数字的方格设置对应一种颜色
num = [0, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]   #判断数字
a = [[0, 2, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]#初始矩阵，可以随机产生一个，只需要调用随机生成的几行代码
#循环打印出画布，将数字矩阵显示，对应的颜色数字
for i in range(0, 4):
    for j in range(0, 4):
        num_index=num.index(a[i][j])
        if a[i][j] == 0:
            canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100, fill='burlywood',
                                    outline='wheat')
        else:
            canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100, fill=num_color[num_index],
                                    outline='wheat')  # outline='blue'
            canvas.create_text(100 * j + 55, 100 * i + 55, text=a[i][j], font=('Time New Roman', 35),
                               fill='maroon')
canvas.pack()
print(np.array(a))
def up():
    global a                        #设为全局变量，实现不同按钮之间可以循环使用a
    b=[]
    # 我们将所有的需要计算的矩阵，计算方向全都转化为在行方向，从左到右的计算方式进行，简化计算
    #不同的方向转化的方式也不相同，有难有易
    for i in range(0,4):
        b.append([])
        for j in range(0,4):
            b[i].append(a[j][i])
    # print('切换',np.array(b))
    #在每一个方向的计算之前都进行转化，之后就可以使用下面的计算方法
    #首先将数据进行集中，非零数据靠左，方便进行计算。
    #采用的方法是，从左向右遍历，若有零则删去第一个零，末尾添加一个零，代表零的后移。
    for i in range(0,4):
        for j in range(0,4):
            if b[i][j]==0:
                b[i].remove(0)
                b[i].append(0)
    #从左向右计算将每一种情况都检查一遍，进行计算。
    for i in range(0, 4):
        if b[i][0] == b[i][1]:
            b[i][0] = 2 * b[i][0]
            if b[i][2] == b[i][3]:
                b[i][1] = 2 * b[i][2]
                b[i][2] = 0
                b[i][3] = 0
            else:
                b[i][1] = b[i][2]
                b[i][2] = b[i][3]
                b[i][3] = 0
        elif b[i][1] == b[i][2]:
            b[i][1] = 2 * b[i][1]
            b[i][2] = 0
            # b[i][3] = 0
        elif b[i][1] != b[i][2]:
            if b[i][2] == b[i][3]:
                b[i][2] = 2 * b[i][2]
                b[i][3] = 0
    # print('计算', np.array(a))
    #计算完以后，我们需要还原之前转化的矩阵，还原到他应该展示的视角。并且还给a，保证后续的操作顺利
    a=[]
    for i in range(0,4):
        a.append([])
        for j in range(0,4):
            a[i].append(b[j][i])
    # 随机选择一个元素为零的地址，随机选择2或4，进行替换
    r_i = []
    r_j = []
    for i in range(0, 4):
        for j in range(0, 4):
            if a[i][j] == 0:
                r_i.append(i)
                r_j.append(j)
    index_random = random.randint(0, len(r_i) - 1)  # 产生一个元素为零的随机地址
    index_num = random.choice([2, 4])  # 随机产生一个数字2或4
    a[r_i[index_random]][r_j[index_random]] = index_num  # 替换对应位置的数字
    print(np.array(a))
    for i in range(0, 4):
        for j in range(0, 4):
            num_index = num.index(a[i][j])
            if a[i][j] == 0:
                canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100, fill='burlywood',
                                        outline='wheat')
            else:
                canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100,
                                        fill=num_color[num_index],
                                        outline='wheat')  # outline='blue'
                canvas.create_text(100 * j + 55, 100 * i + 55, text=a[i][j], font=('Time New Roman', 35),
                                   fill='maroon')

def down():
    global a
    b=[[],[],[],[]]
    for i in range(0,4):
        for j in range(3,-1,-1):
            b[i].append(a[j][i])
    # print('切换',np.array(b))
    for i in range(0,4):
        for j in range(0,4):
            if b[i][j]==0:
                b[i].remove(0)
                b[i].append(0)
    # print('集中', np.array(b))
    for i in range(0, 4):
        if b[i][0] == b[i][1]:
            b[i][0] = 2 * b[i][0]
            if b[i][2] == b[i][3]:
                b[i][1] = 2 * b[i][2]
                b[i][2] = 0
                b[i][3] = 0
            else:
                b[i][1] = b[i][2]
                b[i][2] = b[i][3]
                b[i][3] = 0
        elif b[i][1] == b[i][2]:
            b[i][1] = 2 * b[i][1]
            b[i][2] = 0
            # b[i][3] = 0
        elif b[i][1] != b[i][2]:
            if b[i][2] == b[i][3]:
                b[i][2] = 2 * b[i][2]
                b[i][3] = 0
    # print('计算', np.array(b))
    a=[]
    i=0
    for j in range(3,-1,-1):
        a.append([])
        for k in range(0,4):
            a[i].append(b[k][j])
        i=i+1
    r_i = []
    r_j = []
    for i in range(0, 4):
        for j in range(0, 4):
            if a[i][j] == 0:
                r_i.append(i)
                r_j.append(j)
    index_random = random.randint(0, len(r_i) - 1)  # 产生一个元素为零的随机地址
    index_num = random.choice([2, 4])  # 随机产生一个数字2或4
    a[r_i[index_random]][r_j[index_random]] = index_num  # 替换对应位置的数字
    print(np.array(a))
    for i in range(0, 4):
        for j in range(0, 4):
            num_index = num.index(a[i][j])
            if a[i][j] == 0:
                canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100, fill='burlywood',
                                        outline='wheat')
            else:
                canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100,
                                        fill=num_color[num_index],
                                        outline='wheat')  # outline='blue'
                canvas.create_text(100 * j + 55, 100 * i + 55, text=a[i][j], font=('Time New Roman', 35),
                                   fill='maroon')

def left():
    global a
    b=a
    # print('切换',np.array(b))
    for i in range(0,4):
        for j in range(0,4):
            if b[i][j]==0:
                b[i].remove(0)
                b[i].append(0)
    for i in range(0, 4):
        if b[i][0] == b[i][1]:
            b[i][0] = 2 * b[i][0]
            if b[i][2] == b[i][3]:
                b[i][1] = 2 * b[i][2]
                b[i][2] = 0
                b[i][3] = 0
            else:
                b[i][1] = b[i][2]
                b[i][2] = b[i][3]
                b[i][3] = 0
        elif b[i][1] == b[i][2]:
            b[i][1] = 2 * b[i][1]
            b[i][2] = 0
            # b[i][3] = 0
        elif b[i][1] != b[i][2]:
            if b[i][2] == b[i][3]:
                b[i][2] = 2 * b[i][2]
                b[i][3] = 0
    # print('计算', np.array(a))
    a=b
    r_i = []
    r_j = []
    for i in range(0, 4):
        for j in range(0, 4):
            if a[i][j] == 0:
                r_i.append(i)
                r_j.append(j)
    index_random = random.randint(0, len(r_i) - 1)  # 产生一个元素为零的随机地址
    index_num = random.choice([2, 4])  # 随机产生一个数字2或4
    a[r_i[index_random]][r_j[index_random]] = index_num  # 替换对应位置的数字
    print(np.array(a))
    for i in range(0, 4):
        for j in range(0, 4):
            num_index = num.index(a[i][j])
            if a[i][j] == 0:
                canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100, fill='burlywood',
                                        outline='wheat')

            else:
                canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100,
                                        fill=num_color[num_index],
                                        outline='wheat')  # outline='blue'
                canvas.create_text(100 * j + 55, 100 * i + 55, text=a[i][j], font=('Time New Roman', 35),
                                   fill='maroon')


def right():
    global a
    b=[]
    for i in range(0,4):
        b.append([])
        for j in range(3,-1,-1):
            b[i].append(a[i][j])
    # print('切换',np.array(b))
    for i in range(0,4):
        for j in range(0,4):
            if b[i][j]==0:
                b[i].remove(0)
                b[i].append(0)
    for i in range(0, 4):
        if b[i][0] == b[i][1]:
            b[i][0] = 2 * b[i][0]
            if b[i][2] == b[i][3]:
                b[i][1] = 2 * b[i][2]
                b[i][2] = 0
                b[i][3] = 0
            else:
                b[i][1] = b[i][2]
                b[i][2] = b[i][3]
                b[i][3] = 0
        elif b[i][1] == b[i][2]:
            b[i][1] = 2 * b[i][1]
            b[i][2] = 0
            # b[i][3] = 0   #不需要进行管理
        elif b[i][1] != b[i][2]:
            if b[i][2] == b[i][3]:
                b[i][2] = 2 * b[i][2]
                b[i][3] = 0
    # print('计算', np.array(a))
    a=[]
    for i in range(0,4):
        a.append([])
        for j in range(3,-1,-1):
            a[i].append(b[i][j])
    r_i = []
    r_j = []
    for i in range(0, 4):
        for j in range(0, 4):
            if a[i][j] == 0:
                r_i.append(i)
                r_j.append(j)
    index_random = random.randint(0, len(r_i) - 1)  # 产生一个元素为零的随机地址
    index_num = random.choice([2, 4])  # 随机产生一个数字2或4
    a[r_i[index_random]][r_j[index_random]] = index_num  # 替换对应位置的数字
    print(np.array(a))
    for i in range(0, 4):
        for j in range(0, 4):
            num_index = num.index(a[i][j])
            if a[i][j] == 0:
                canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100, fill='burlywood',
                                        outline='wheat')

            else:
                canvas.create_rectangle(100 * j + 10, 100 * i + 10, 100 * j + 100, 100 * i + 100,
                                        fill=num_color[num_index],
                                        outline='wheat')  # outline='blue'
                canvas.create_text(100 * j + 55, 100 * i + 55, text=a[i][j], font=('Time New Roman', 35),
                                   fill='maroon')


    canvas.pack()

#上下左右按钮，实现操作的调用
button1 = tk.Button(win, text="上", font=('楷体', 20), command=lambda:up())
button1.pack()
button2 = tk.Button(win, text="下", font=('楷体', 20), command=lambda:down())
button2.pack()
button1.bind("up", lambda:up())
button3 = tk.Button(win, text="左", font=('楷体', 20), command=lambda:left())
button3.pack()
button4 = tk.Button(win, text="右", font=('楷体', 20), command=lambda:right())
button4.pack()
win.mainloop()









