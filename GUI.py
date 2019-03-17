from tkinter import *
import tkinter.messagebox
import pvp_engine
import time


turn = 1
stop = 0
x_ed_1 = 0 
y_ed_1 = 0 
x_ed_2 = 0 
y_ed_2 = 0 
choice_1 = 0
 

def paint(x, y):
    global turn, stop, x_ed_1, x_ed_2, y_ed_1, y_ed_2
    x1, y1 = (x * 30 - 12), (y * 30 - 12)
    x2, y2 = (x * 30 + 12), (y * 30 + 12)
    decide_1 = pvp_engine.decide_1(x, y)
    if stop == 0:
        if decide_1 == 1:
            if turn % 2 == 1:
                pvp_engine.black(x, y)
                canvas.create_rectangle(x1 - 2, y1 - 2, x2 + 2, y2 + 2, fill = "goldenrod", outline = "red", width = 3, tags = ("chess", "a" + str(turn), "b" + str(turn)))
                canvas.create_oval(x1, y1, x2, y2, fill = "black", tags = ("chess", "a" + str(turn)))
                canvas.create_text(x*30,y*30, text = turn, fill = "white", tags = ("chess", "a" + str(turn)))
                canvas.delete("b" + str(turn - 1))
                x_ed_1 = x
                y_ed_1 = y
                canvas.create_oval(30, 30, 80, 80, fill = "white", outline ="white", tags = ("chess", "a" + str(turn)))
            elif turn % 2 == 0:
                pvp_engine.white(x, y)
                canvas.create_rectangle(x1 - 2, y1 - 2, x2 + 2, y2 + 2, fill = "goldenrod", outline = "red", width = 3, tags = ("chess", "a" + str(turn), "b" + str(turn)))
                canvas.create_oval(x1, y1, x2, y2, fill = "white", outline ="white", tags = ("chess", "a" + str(turn)))
                canvas.create_text(x*30,y*30, text = turn, fill = "black", tags = ("chess", "a" + str(turn)))
                canvas.delete("b" + str(turn - 1))
                x_ed_2 = x
                y_ed_2 = y 
                canvas.create_oval(30, 30, 80, 80, fill = "black", tags = ("chess", "a" + str(turn)))
            over = pvp_engine.judge(x, y)
            if over == 1:
                if turn % 2 == 1:
                    tkinter.messagebox.showinfo("","游戏结束了,黑棋获胜")
                elif turn % 2 == 0:
                    tkinter.messagebox.showinfo("","游戏结束了,白棋获胜")
                stop = 1
            elif over == 2:
                tkinter.messagebox.showinfo("","游戏结束了,和局")
                stop = 1
            elif over == 3:
                tkinter.messagebox.showinfo("","黑棋禁手，白棋获胜")
                stop = 1
            turn = turn + 1


def humman_position(event):
    if event.x % 30 > 15:
        x = event.x // 30 + 1
    else:
        x = event.x // 30
    if event.y % 30 >15:
        y = event.y // 30 + 1
    else:
        y = event.y// 30
    if x > 18:
        x = 18
    if y > 18:
        y = 18 
    if x < 4:
        x = 4
    if y < 4:
        y = 4   
    paint(x, y)
    AI_position()

def AI_position():
    x, y = pvp_engine.getscore()
    paint(x, y)

def AIvsAI():
    while stop == 0:
        x, y = pvp_engine.getscore()
        paint(x, y)
        time.sleep(3)




def modle_choice():
    global turn, stop, choice_1
    if var_1.get() == 0:
        canvas.bind("<Button-1>", humman_position)
    elif var_1.get() == 1:
        if var_2.get() == 0:
            choice_1 = 0
        elif var_2.get() == 1:
            choice_1 = 1
        while choice_1 == 0:
            AI_position()
            choice_1 = 1
        else:
            canvas.bind("<Button-1>", humman_position)
            choice_1 = 0
    elif var_1.get() == 2:
        AIvsAI()
        

def moveback():
    global turn, x_ed_1, x_ed_2, y_ed_1, y_ed_2
    canvas.delete("a" + str(turn - 1))
    canvas.delete("a" + str(turn - 2))
    pvp_engine.moveback(x_ed_1, y_ed_1)
    pvp_engine.moveback(x_ed_2, y_ed_2)
    turn = turn - 2


def restart():
    global turn, stop 
    canvas.delete("chess")
    turn = 1
    stop = 0
    pvp_engine.restart()
    

window = Tk()
window.title("Kiki Gomoku")
window.geometry("900x700")

canvas = Canvas(window, width = 900, height = 900, bg = "plum")
canvas.pack(expand = YES, fill = BOTH)


canvas.create_rectangle(100, 100, 560, 560, fill = "goldenrod", outline = "goldenrod" )

canvas.create_oval(327, 327, 333, 333, fill = "black")
canvas.create_oval(207, 207, 213, 213, fill = "black")
canvas.create_oval(207, 447, 213, 453, fill = "black")
canvas.create_oval(447, 207, 453, 213, fill = "black")
canvas.create_oval(447, 447, 453, 453, fill = "black")

for i in range(4, 19):
    canvas.create_text(i*30, 90, text = chr(61 + i), font = ("Arial", 12))

for i in range(4, 19):
    canvas.create_text(90, i*30, text = i-3, font = ("Arial", 12))

for i in range(4, 19):
    canvas.create_line(i*30, 120, i*30, 540, width = 1)

for i in range(4, 19):
    canvas.create_line(120, i*30, 540, i*30, width = 1)


var_1 = IntVar() 
choice_pvp1 = Radiobutton(window, text = "人人对战", font = ("楷体", 15, "bold"), variable = var_1, value = 0, bg = "skyblue", command = modle_choice)
choice_pvp2 = Radiobutton(window, text = "人机对战", font = ("楷体", 15, "bold"), variable = var_1, value = 1, bg = "skyblue", command = modle_choice)
choice_pvp3 = Radiobutton(window, text = "机机对战", font = ("楷体", 15, "bold"), variable = var_1, value = 2, bg = "skyblue", command = modle_choice)
choice_pvp3.place(x = 640, y = 195, width = 200, height = 50)
choice_pvp1.place(x = 640, y = 245, width = 200, height = 50)
choice_pvp2.place(x = 640, y = 295, width = 200, height = 50)


var_2 = IntVar() 
choice_pve1 = Radiobutton(window, text = "AI持黑", font = ("楷体", 15, "bold"), variable = var_2, value = 0, bg = "lime", command = modle_choice)
choice_pve2 = Radiobutton(window, text = "AI持白", font = ("楷体", 15, "bold"), variable = var_2, value = 1, bg = "lime", command = modle_choice)
choice_pve1.place(x = 640, y = 345, width = 200, height = 50)
choice_pve2.place(x = 640, y = 395, width = 200, height = 50)


button_1 = Button(window, text = "悔棋", font = ("楷体", 15, "bold"), bg = "yellow", command = moveback)
button_1.place(x = 640, y = 445, width = 100, height = 50)


button_2 = Button(window, text = "重玩", font = ("楷体", 15, "bold"), bg = "hotpink", command = restart)
button_2.place(x = 740, y = 445, width = 100, height = 50)



window.mainloop()

