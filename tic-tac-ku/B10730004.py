import tkinter as tk
from tkinter import messagebox
from functools import partial

def init():
    global curPlayer
    global pos
    global EndBlock
    global selectedButton
    global blocks
    global win
    global peace
    curPlayer = -1
    pos = -1
    EndBlock = [0,0,0,0,0,0,0,0,0]
    selectedButton = []
    for i in range(9):
        selectedButton.append([0,0,0,0,0,0,0,0,0])
    blocks = []
    for i in range(9):
        blocks.append([])
        for j in range(9):
            temp = tk.Button(window,text=" ",bg="snow",width=6,height=2,command=partial(motion,i,j))
            blocks[i].append(temp)
            blocks[i][j].place(x=50 + (i % 3) * 156 + (j % 3) * 51,y=50 + int(i / 3) * 124 + int(j / 3) * 40,anchor="nw")
    win = 0
    peace = 0
    canvas.create_image(4,4,anchor="nw",image=PlayerImage[curPlayer + 1])
    canvasPos.create_image(4,4,anchor="nw",image=PosImage[pos + 1])

def motion(i,j):
    global pos
    global EndBlock
    global selectedButton
    global blocks
    global curPlayer
    global canvas
    if pos == -1 or pos == i:
        if win == 1:
            BigWin()
        elif peace == 1:
            BigPeace()
        elif EndBlock[i] != 0:
            tk.messagebox.showerror(title="Illegal Block Selected",message="這裡已經被攻佔囉！\n請選擇其他區域")
        elif selectedButton[i][j] != 0:
            tk.messagebox.showerror(title="Illegal Button Selected",message="有人選過這個位置囉！\n請選擇其他位置")
        else:
            blocks[i][j]["text"] = player[curPlayer + 1]
            selectedButton[i][j] = curPlayer
            blockWin(i)
            BigWin()
            BigPeace()
            if win == 0 and peace == 0:
                curPlayer*=-1
                canvas.create_image(4,4,anchor="nw",image=PlayerImage[curPlayer + 1])
                if EndBlock[j] != 0 or blockPeace(j):
                    pos = -1
                else:
                    pos = j
                canvasPos.create_image(4,4,anchor="nw",image=PosImage[pos + 1])
    else:
        tk.messagebox.showerror(title="Illegal Block Selected",message="這裡不是現在該下的區域呦！")


def blockWin(i):
    global blocks
    global EndBlock
    global selectedButton
    if (selectedButton[i][0] == curPlayer and selectedButton[i][1] == curPlayer and selectedButton[i][2] == curPlayer) or \
        (selectedButton[i][3] == curPlayer and selectedButton[i][4] == curPlayer and selectedButton[i][5] == curPlayer) or \
        (selectedButton[i][6] == curPlayer and selectedButton[i][7] == curPlayer and selectedButton[i][8] == curPlayer) or \
        (selectedButton[i][0] == curPlayer and selectedButton[i][3] == curPlayer and selectedButton[i][6] == curPlayer) or \
        (selectedButton[i][1] == curPlayer and selectedButton[i][4] == curPlayer and selectedButton[i][7] == curPlayer) or \
        (selectedButton[i][2] == curPlayer and selectedButton[i][5] == curPlayer and selectedButton[i][8] == curPlayer) or \
        (selectedButton[i][0] == curPlayer and selectedButton[i][4] == curPlayer and selectedButton[i][8] == curPlayer) or \
        (selectedButton[i][2] == curPlayer and selectedButton[i][4] == curPlayer and selectedButton[i][6] == curPlayer):
        EndBlock[i] = curPlayer
        for j in range(9):
            blocks[i][j]["text"] = " "
            selectedButton[i][j] = curPlayer
        if curPlayer == -1:
            blocks[i][0]["bg"] = "black"
            blocks[i][2]["bg"] = "black"
            blocks[i][4]["bg"] = "black"
            blocks[i][6]["bg"] = "black"
            blocks[i][8]["bg"] = "black"
        else:
            blocks[i][0]["bg"] = "black"
            blocks[i][1]["bg"] = "black"
            blocks[i][2]["bg"] = "black"
            blocks[i][3]["bg"] = "black"
            blocks[i][5]["bg"] = "black"
            blocks[i][6]["bg"] = "black"
            blocks[i][7]["bg"] = "black"
            blocks[i][8]["bg"] = "black"

def blockPeace(i):
    for j in range(9):
        if selectedButton[i][j] == 0:
            return False
    return True

def BigWin():
    global win
    if (EndBlock[0] == curPlayer and EndBlock[1] == curPlayer and EndBlock[2] == curPlayer) or \
        (EndBlock[3] == curPlayer and EndBlock[4] == curPlayer and EndBlock[5] == curPlayer) or \
        (EndBlock[6] == curPlayer and EndBlock[7] == curPlayer and EndBlock[8] == curPlayer) or \
        (EndBlock[0] == curPlayer and EndBlock[3] == curPlayer and EndBlock[6] == curPlayer) or \
        (EndBlock[1] == curPlayer and EndBlock[4] == curPlayer and EndBlock[7] == curPlayer) or \
        (EndBlock[2] == curPlayer and EndBlock[5] == curPlayer and EndBlock[8] == curPlayer) or \
        (EndBlock[0] == curPlayer and EndBlock[4] == curPlayer and EndBlock[8] == curPlayer) or \
        (EndBlock[2] == curPlayer and EndBlock[4] == curPlayer and EndBlock[6] == curPlayer) or win == 1:
        tk.messagebox.showinfo(title="Winner is " + player[curPlayer + 1],message="恭喜玩家 " + player[curPlayer + 1] + " 取得勝利！\n 要重新開始請按棋盤下方重新整理")
        win = 1
def BigPeace():
    global peace
    temp = True
    for i in range(9):
        for j in range(9):
            if selectedButton[i][j] == 0:
                temp = False
    if temp or peace == 1:
        tk.messagebox.showinfo(title="It's a Tie <3",message="兩位都是高手呢！\n 要重新開始請按棋盤下方重新整理")
        peace = 1


window = tk.Tk()
window.title("Tic-Tac-Ku")
window.geometry("750x500")
window.configure(background='moccasin')
player = ["X","","O"]
win = 0
peace = 0
curPlayer = -1
pos = -1
EndBlock = [0,0,0,0,0,0,0,0,0]
selectedButton = []
for i in range(9):
    selectedButton.append([0,0,0,0,0,0,0,0,0])

blocks = []
for i in range(9):
    blocks.append([])
    for j in range(9):
        temp = tk.Button(window,text=" ",bg="snow",width=6,height=2,command=partial(motion,i,j))
        blocks[i].append(temp)
        blocks[i][j].place(x=50 + (i % 3) * 156 + (j % 3) * 51,y=50 + int(i / 3) * 124 + int(j / 3) * 40,anchor="nw")

curPlayerLabel = tk.Label(window,text="  現在輪到：",bg="gray",font=(24),anchor="w",width=15,height=2)
curPlayerLabel.place(x=550,y=30,anchor="nw")
PlayerImage = [tk.PhotoImage(file="X.gif"),"",tk.PhotoImage(file="O.gif")]
canvas = tk.Canvas(window,bg="gray",width=174,height=167)
canvas.place(x=548,y=80,anchor="nw")
canvas.create_image(4,4,anchor="nw",image=PlayerImage[curPlayer + 1])

curPosLabel = tk.Label(window,text="  現在位置：",bg="gray",font=(24),anchor="w",width=15,height=2)
curPosLabel.place(x=550,y=260,anchor="nw")
PosImage = [tk.PhotoImage(file="-1.gif"),tk.PhotoImage(file="0.gif"),tk.PhotoImage(file="1.gif"),tk.PhotoImage(file="2.gif"),tk.PhotoImage(file="3.gif"),tk.PhotoImage(file="4.gif"),tk.PhotoImage(file="5.gif"),tk.PhotoImage(file="6.gif"),tk.PhotoImage(file="7.gif"),tk.PhotoImage(file="8.gif")]
canvasPos = tk.Canvas(window,bg="gray",width=174,height=167)
canvasPos.place(x=548,y=310,anchor="nw")
canvasPos.create_image(4,4,anchor="nw",image=PosImage[pos + 1])

haha = tk.Button(window,text="重新整理",bg="snow",width=8,height=2,command=init)
haha.place(x=50,y=430,anchor="nw")
    

window.mainloop()