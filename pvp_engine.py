import numpy as np
import random as rd
chess = [[5 for i in range(23)] for i in range(23)]
for i in range(4, 19):
    for j in range(4, 19):
        chess[i][j] = 0



a = [[1, 0], [0, 1], [1, 1], [1, -1]]
b = [1,-1]




def decide_1(x, y):
    if chess[x][y] == 0:
        return 1
    else:
        return 0

def black(x, y):
    chess[x][y] = 1

def white(x, y):
    chess[x][y] = 2


def judge(x, y):
    full = 0
    over = 0
    for m in range(4, 19):
        for n in range(4, 19):
            if chess[m][n] != 0:
                full = full + 1
    if chess[x][y] == 1:
        a0, a1, a2, a3, a4, a5, a6, a7, a8 = chesscount(x, y, 1)
        if a1 + a2 > 1 or a3 > 1:
            over = 3
    for i in range(4):
        wcount = 1
        bcount = 1
        empty = 0
        for j in range(2):
            for k in range(1,5):
                _x = x + b[j] * a[i][0] * k
                _y = y + b[j] * a[i][1] * k
                if chess[x][y] == 2:
                    if chess[_x][_y] == 2:
                        wcount = wcount + 1
                    else:
                        break
                elif chess[x][y] == 1:
                    if chess[_x][_y] == 1:
                        bcount = bcount + 1
                    else:
                        break
        if wcount > 4 or bcount == 5:
            over = 1
            break
        elif bcount > 5:
            over = 3
            continue
    if over != 1 or over != 3:
        if full > 224:
            over = 2
    return over


def restart():
    for i in range(4, 19):
        for j in range(4, 19):
            chess[i][j] = 0

def moveback(x, y):
    chess[x][y] = 0









def chesscount(x, y, z):
    f = [1, 0, 1, 1]
    g = [0, 1, 1, -1] 
    five = livefour = four = livethree = three = livetwo = two = liveone = one = 0
    for i in range(4):
        if   (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == z and chess[x + 4 * f[i]][y + 4 * g[i]] == z) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == z) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x + f[i]][y + g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 4 * f[i]][y - 4 * g[i]] == z) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x + f[i]][y + g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == z):
            five = five + 1

        elif (chess[x - f[i]][y - g[i]] == 0 and chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == z and chess[x + 4 * f[i]][y + 4 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x + f[i]][y + g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x - 3 * f[i]][y - 3 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x + f[i]][y + g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == z and chess[x - 4 * f[i]][y - 4 * g[i]] == 0):
            livefour = livefour + 1

        elif (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == z and chess[x + 4 * f[i]][y + 4 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == z and chess[x - 1 * f[i]][y - 1 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x - 1 * f[i]][y - 1 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x - 1 * f[i]][y - 1 * g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x - 1 * f[i]][y - 1 * g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == z) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 1 * f[i]][y - 1 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == 0 and chess[x - 1 * f[i]][y - 1 * g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == z) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == z and chess[x - 4 * f[i]][y - 4 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == 0 and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 4 * f[i]][y + 4 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == z) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x + 3 * f[i]][y + 3 * g[i]] == z and chess[x + 4 * f[i]][y + 4 * g[i]] == z) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == 0 and chess[x + 4 * f[i]][y + 4 * g[i]] == z) \
        or   (chess[x - f[i]][y - g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == z and chess[x - 4 * f[i]][y - 4 * g[i]] == z) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == 0 and chess[x - 3 * f[i]][y - 3 * g[i]] == z and chess[x - 4 * f[i]][y - 4 * g[i]] == z) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == 0 and chess[x - 4 * f[i]][y - 4 * g[i]] == z) \
        or   (chess[x + f[i]][y + g[i]] == 0 and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == z and chess[x - 1 * f[i]][y - 1 * g[i]] == z) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x + 3 * f[i]][y + 3 * g[i]] == z and chess[x - 1 * f[i]][y - 1 * g[i]] == z) \
        or   (chess[x + f[i]][y + g[i]] == 0 and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x - 1 * f[i]][y - 1 * g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == z) \
        or   (chess[x - f[i]][y - g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == z and chess[x + 1 * f[i]][y + 1 * g[i]] == z) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == 0 and chess[x - 3 * f[i]][y - 3 * g[i]] == z and chess[x + 1 * f[i]][y + 1 * g[i]] == z) \
        or   (chess[x - f[i]][y - g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x + 1 * f[i]][y + 1 * g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z): 
            four = four + 1

        elif (chess[x - f[i]][y - g[i]] == 0 and chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x + f[i]][y + g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == 0 and chess[x + f[i]][y + g[i]] == 0 and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == z and chess[x + 4 * f[i]][y + 4 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == 0 and chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x + 3 * f[i]][y + 3 * g[i]] == z and chess[x + 4 * f[i]][y + 4 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == 0 and chess[x + f[i]][y + g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 4 * f[i]][y - 4 * g[i]] == 0 and chess[x - 3 * f[i]][y - 3 * g[i]] == z) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x + f[i]][y + g[i]] == 0 and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == 0 and chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x - 3 * f[i]][y - 3 * g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == z) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x + f[i]][y + g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == 0 and chess[x - 3 * f[i]][y - 3 * g[i]] == z and chess[x - 4 * f[i]][y - 4 * g[i]] == 0):
            livethree = livethree + 1

        elif (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == 0 and chess[x + 4 * f[i]][y + 4 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x + 3 * f[i]][y + 3 * g[i]] == 0 and chess[x - 1 * f[i]][y - 1 * g[i]] == z) \
        or   (chess[x + f[i]][y + g[i]] == 0 and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x - 1 * f[i]][y - 1 * g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == z) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x - 1 * f[i]][y - 1 * g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == 0 and chess[x - 1 * f[i]][y - 1 * g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 4 * f[i]][y - 4 * g[i]] == 0 and chess[x - 3 * f[i]][y - 3 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == 0 and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == z and chess[x + 4 * f[i]][y + 4 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x + 3 * f[i]][y + 3 * g[i]] == z and chess[x + 4 * f[i]][y + 4 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == 0 and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == z and chess[x - 1 * f[i]][y - 1 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x + 3 * f[i]][y + 3 * g[i]] == z and chess[x - 1 * f[i]][y - 1 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == 0 and chess[x - 1 * f[i]][y - 1 * g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == z) \
        or   (chess[x + f[i]][y + g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == 0 and chess[x - 3 * f[i]][y - 3 * g[i]] == z and chess[x - 1 * f[i]][y - 1 * g[i]] == z) \
        or   (chess[x - f[i]][y - g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == z and chess[x - 4 * f[i]][y - 4 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == 0 and chess[x - 3 * f[i]][y - 3 * g[i]] == z and chess[x - 4 * f[i]][y - 4 * g[i]] == 0): 
            three = three + 1
        
        elif (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x + 3 * f[i]][y + 3 * g[i]] == 0 and chess[x - 1 * f[i]][y - 1 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == 0 and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == 0 and chess[x - 1 * f[i]][y - 1 * g[i]] == z) \
        or   (chess[x + f[i]][y + g[i]] == 0 and chess[x - 1 * f[i]][y - 1 * g[i]] == 0 and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == 0 and chess[x - 1 * f[i]][y - 1 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == 0 and chess[x + 1 * f[i]][y + 1 * g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == 0 and chess[x - 3 * f[i]][y - 3 * g[i]] == 0 and chess[x + 1 * f[i]][y + 1 * g[i]] == 0):
            livetwo = livetwo + 1

        elif (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x + 3 * f[i]][y + 3 * g[i]] == 0 and chess[x + 4 * f[i]][y + 4 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == 0 and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x + 3 * f[i]][y + 3 * g[i]] == 0 and chess[x - 1 * f[i]][y - 1 * g[i]] == z) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x - 1 * f[i]][y - 1 * g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == 0 and chess[x - 3 * f[i]][y - 3 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == 0 and chess[x - 3 * f[i]][y - 3 * g[i]] == 0 and chess[x - 4 * f[i]][y - 4 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == 0 and chess[x - 1 * f[i]][y - 1 * g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == 0 and chess[x + 2 * f[i]][y + 2 * g[i]] == z) \
        or   (chess[x + f[i]][y + g[i]] == 0 and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 1 * f[i]][y - 1 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == 0 and chess[x - 4 * f[i]][y - 4 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == 0 and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == 0 and chess[x + 4 * f[i]][y + 4 * g[i]] == 0):
            two = two + 1

        elif (chess[x + f[i]][y + g[i]] == 0 and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x - 1 * f[i]][y - 1 * g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == 0):
            liveone = liveone + 1

        elif (chess[x + f[i]][y + g[i]] == 0 and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x + 3 * f[i]][y + 3 * g[i]] == 0 and chess[x + 4 * f[i]][y + 4 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == 0 and chess[x - 3 * f[i]][y - 3 * g[i]] == 0 and chess[x - 4 * f[i]][y - 4 * g[i]] == 0):
            one = one + 1
    return five, livefour, four, livethree, three, livetwo, two, liveone, one
         
        
                
def evaluate(c):
    score = 0
    for i in range(4, 19):
        for j in range(4, 19):
            wscore = 0
            bscore = 0
            a0 = a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = 0
            b0 = b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = 0
            if chess[i][j] == 0:
                continue
            elif chess[i][j] == 1:
                a0, a1, a2, a3, a4, a5, a6, a7, a8 = chesscount(i, j, 1)
            elif chess[i][j] == 2:
                b0, b1, b2, b3, b4, b5, b6, b7, b8 = chesscount(i, j, 2)
            if a1 + a2 > 1 or a3 > 1:
                bscore = 0
            else:
                bscore = 1000000 * a0 + 100000 * a1 + 1000 * (a2 + a3) + 100 * (a4 + a5) + 10 * (a6 + a7) + a8
            wscore = 1000000 * a0 + 100000 * b1 + 1000 * (b2 + b3) + 100 * (b4 + b5) + 10 * (b6 + b7) + b8
            if c == 1:
                score = score + bscore - wscore * 2
            elif c == 2:
                score = score + wscore - bscore * 2
    return score





def AI_1b():
    bscoreboard = np.array([[-10000000 for i in range(23)]for i in range(23)])
    wscoreboard = np.array([[-10000000 for i in range(23)]for i in range(23)])
    boundary_x = []
    boundary_y = []
    if chess[11][11] == 0:
        p, q = 11, 11
    else:
        for u in range(4, 19):
            for v in range(4, 19):
                if chess[u][v] == 1 or chess[u][v] == 2:
                    boundary_x.append(u)
                    boundary_y.append(v)
        x1 = max(4, min(boundary_x)-1)
        y1 = max(4, min(boundary_y)-1)
        x2 = min(19,max(boundary_x)+2)
        y2 = min(19,max(boundary_y)+2)
        over_1 = 0
        over_2 = 0
        for x in range(x1, x2):
            for y in range(y1, y2):
                if chess[x][y] == 0:
                    chess[x][y] = 1
                    over = judge(x, y)
                    if over == 1 or over == 2:
                        chess[x][y] = 0
                        over_1 = 1
                        c, d = x, y
                        break
                    elif over == 3:
                        chess[x][y] = 0
                        continue
                    else:
                        chess[x][y] = 2
                        over = judge(x, y)
                        if over == 1 or over == 2:
                            chess[x][y] = 0
                            over_2 = 1
                            e, f = x, y
                            break
                        else:
                            wscore = 0
                            bscore = 0
                            chess[x][y] = 0
                            a0, a1, a2, a3, a4, a5, a6, a7, a8 = chesscount(x, y, 1)
                            b0, b1, b2, b3, b4, b5, b6, b7, b8 = chesscount(x, y, 2)
                            bscore = 200000 * a1 + 1000 * (a2 + a3) + 100 * (a4 + a5) + 10 * (a6 + a7) + a8
                            wscore = 100000 * b1 + 1000 * (b2 + b3) + 100 * (b4 + b5) + 10 * (b6 + b7) + b8
                            bscoreboard[x][y] = bscore
                            wscoreboard[x][y] = wscore
        if over_1 == 1:
            p, q = c, d
        elif over_2 == 1:
            p, q = e, f
        else:
            position = []
            for i in range(23):
                for j in range(23):
                    if np.max(bscoreboard) >= np.max(wscoreboard):
                        if bscoreboard[i][j] == np.max(bscoreboard):
                            position.append(i * 23 + j)
                    elif np.max(bscoreboard) < np.max(wscoreboard):
                        if wscoreboard[i][j] == np.max(wscoreboard):
                            position.append(i * 23 + j)
            z = rd.choice(position)
            p = z // 23
            q = z % 23
    return p, q   



def AI_1w():
    bscoreboard = np.array([[-10000000 for i in range(23)]for i in range(23)])
    wscoreboard = np.array([[-10000000 for i in range(23)]for i in range(23)])
    boundary_x = []
    boundary_y = []
    if chess[11][11] == 0:
        p, q = 11, 11
    else:
        for u in range(4, 19):
            for v in range(4, 19):
                if chess[u][v] == 1 or chess[u][v] == 2:
                    boundary_x.append(u)
                    boundary_y.append(v)
        x1 = max(4, min(boundary_x)-1)
        y1 = max(4, min(boundary_y)-1)
        x2 = min(19,max(boundary_x)+2)
        y2 = min(19,max(boundary_y)+2)
        over_1 = 0
        over_2 = 0
        for x in range(x1, x2):
            for y in range(y1, y2):
                if chess[x][y] == 0:
                    chess[x][y] = 2
                    over = judge(x, y)
                    if over == 1 or over == 2:
                        chess[x][y] = 0
                        over_1 = 1
                        c, d = x, y
                        break
                    else:
                        chess[x][y] = 1
                        over = judge(x, y)
                        if over == 1 or over == 2:
                            chess[x][y] = 0
                            over_2 = 1
                            e, f = x, y
                            break
                        else:
                            wscore = 0
                            bscore = 0
                            chess[x][y] = 0
                            a0, a1, a2, a3, a4, a5, a6, a7, a8 = chesscount(x, y, 1)
                            b0, b1, b2, b3, b4, b5, b6, b7, b8 = chesscount(x, y, 2)
                            if a1 + a2 > 1 or a3 > 1:
                                bscore = 0
                            else:
                                bscore = 100000 * a1 + 1000 * (a2 + a3) + 100 * (a4 + a5) + 10 * (a6 + a7) + a8
                            wscore = 200000 * b1 + 1000 * (b2 + b3) + 100 * (b4 + b5) + 10 * (b6 + b7) + b8
                            bscoreboard[x][y] = bscore
                            wscoreboard[x][y] = wscore
        if over_1 == 1:
            p, q = c, d
        elif over_2 == 1:
            p, q = e, f
        else:
            position = []
            for i in range(23):
                for j in range(23):
                    if np.max(bscoreboard) > np.max(wscoreboard):
                        if bscoreboard[i][j] == np.max(bscoreboard):
                            position.append(i * 23 + j)
                    elif np.max(bscoreboard) <= np.max(wscoreboard):
                        if wscoreboard[i][j] == np.max(wscoreboard):
                            position.append(i * 23 + j)
            z = rd.choice(position)
            p = z // 23
            q = z % 23
    return p, q   




def AI_2w():
    scoreboard = np.array([[-10000000 for i in range(23)]for i in range(23)])
    boundary_x = []
    boundary_y = []
    if chess[11][11] == 0:
        p, q = 11, 11
    else:
        for u in range(4, 19):
            for v in range(4, 19):
                if chess[u][v] == 1 or chess[u][v] == 2:
                    boundary_x.append(u)
                    boundary_y.append(v)
        x1 = max(4, min(boundary_x)-1)
        y1 = max(4, min(boundary_y)-1)
        x2 = min(19,max(boundary_x)+2)
        y2 = min(19,max(boundary_y)+2)
        over_1 = 0
        over_2 = 0
        for x in range(x1, x2):
            for y in range(y1, y2):
                score = 0
                if chess[x][y] == 0:
                    chess[x][y] = 2
                    over = judge(x, y)
                    if over == 1 or over == 2:
                        chess[x][y] = 0
                        over_1 = 1
                        c, d = x, y
                        break
                    else:
                        chess[x][y] = 1
                        over = judge(x, y)
                        if over == 1 or over == 2:
                            chess[x][y] = 0
                            over_2 = 1
                            e, f = x, y
                            break
                        else:
                            chess[x][y] = 2
                            scoreboard[x][y] = evaluate(2)
                            chess[x][y] = 0
                            
                            
        if over_1 == 1:
            p, q = c, d
        elif over_2 == 1:
            p, q = e, f
        else:
            position = []
            for i in range(23):
                for j in range(23):
                    if scoreboard[i][j] == np.max(scoreboard):
                        position.append(i * 23 + j)
            z = rd.choice(position)
            p = z // 23
            q = z % 23
    return p, q   



def AI_2b():
    scoreboard = np.array([[-10000000 for i in range(23)]for i in range(23)])
    boundary_x = []
    boundary_y = []
    if chess[11][11] == 0:
        p, q = 11, 11
    else:
        for u in range(4, 19):
            for v in range(4, 19):
                if chess[u][v] == 1 or chess[u][v] == 2:
                    boundary_x.append(u)
                    boundary_y.append(v)
        x1 = max(4, min(boundary_x)-1)
        y1 = max(4, min(boundary_y)-1)
        x2 = min(19,max(boundary_x)+2)
        y2 = min(19,max(boundary_y)+2)
        over_1 = 0
        over_2 = 0
        for x in range(x1, x2):
            for y in range(y1, y2):
                score = 0
                if chess[x][y] == 0:
                    chess[x][y] = 1
                    over = judge(x, y)
                    if over == 1 or over == 2:
                        chess[x][y] = 0
                        over_1 = 1
                        c, d = x, y
                        break
                    elif over == 3:
                        chess[x][y] = 0
                        continue
                    else:
                        chess[x][y] = 2
                        over = judge(x, y)
                        if over == 1 or over == 2:
                            chess[x][y] = 0
                            over_2 = 1
                            e, f = x, y
                            break
                        else:
                            chess[x][y] = 1
                            scoreboard[x][y] = evaluate(1)
                            chess[x][y] = 0
                            
                            
        if over_1 == 1:
            p, q = c, d
        elif over_2 == 1:
            p, q = e, f
        else:
            position = []
            for i in range(23):
                for j in range(23):
                    if scoreboard[i][j] == np.max(scoreboard):
                        position.append(i * 23 + j)
            z = rd.choice(position)
            p = z // 23
            q = z % 23
    return p, q   
  


def AI_3b():
    scoreboard = np.array([[-10000000 for i in range(23)]for i in range(23)])
    boundary_x = []
    boundary_y = []
    if chess[11][11] == 0:
        p, q = 11, 11
    else:
        for u in range(4, 19):
            for v in range(4, 19):
                if chess[u][v] == 1 or chess[u][v] == 2:
                    boundary_x.append(u)
                    boundary_y.append(v)
        x1 = max(4, min(boundary_x)-1)
        y1 = max(4, min(boundary_y)-1)
        x2 = min(19,max(boundary_x)+2)
        y2 = min(19,max(boundary_y)+2)
        over_1 = 0
        over_2 = 0
        for x in range(x1, x2):
            for y in range(y1, y2):
                score = 0
                if chess[x][y] == 0:
                    chess[x][y] = 1
                    over = judge(x, y)
                    if over == 1 or over == 2:
                        chess[x][y] = 0
                        over_1 = 1
                        c, d = x, y
                        break
                    elif over == 3:
                        chess[x][y] = 0
                        continue
                    else:
                        chess[x][y] = 2
                        over = judge(x, y)
                        if over == 1 or over == 2:
                            chess[x][y] = 0
                            over_2 = 1
                            e, f = x, y
                            break
                        else:
                            chess[x][y] = 1
                            g, h = AI_2w()
                            chess[g][h] = 2
                            scoreboard[x][y] = evaluate(1)
                            chess[x][y] = 0
                            chess[g][h] = 0
                            
                            
        if over_1 == 1:
            p, q = c, d
        elif over_2 == 1:
            p, q = e, f
        else:
            position = []
            for i in range(23):
                for j in range(23):
                    if scoreboard[i][j] == np.max(scoreboard):
                        position.append(i * 23 + j)
            z = rd.choice(position)
            p = z // 23
            q = z % 23
    return p, q   
  
  

def AI_3w():
    scoreboard = np.array([[-10000000 for i in range(23)]for i in range(23)])
    boundary_x = []
    boundary_y = []
    if chess[11][11] == 0:
        p, q = 11, 11
    else:
        for u in range(4, 19):
            for v in range(4, 19):
                if chess[u][v] == 1 or chess[u][v] == 2:
                    boundary_x.append(u)
                    boundary_y.append(v)
        x1 = max(4, min(boundary_x)-1)
        y1 = max(4, min(boundary_y)-1)
        x2 = min(19,max(boundary_x)+2)
        y2 = min(19,max(boundary_y)+2)
        over_1 = 0
        over_2 = 0
        for x in range(x1, x2):
            for y in range(y1, y2):
                score = 0
                if chess[x][y] == 0:
                    chess[x][y] = 2
                    over = judge(x, y)
                    if over == 1 or over == 2:
                        chess[x][y] = 0
                        over_1 = 1
                        c, d = x, y
                        break
                    else:
                        chess[x][y] = 1
                        over = judge(x, y)
                        if over == 1 or over == 2:
                            chess[x][y] = 0
                            over_2 = 1
                            e, f = x, y
                            break
                        else:
                            chess[x][y] = 2
                            g, h = AI_2b()
                            chess[g][h] = 1
                            scoreboard[x][y] = evaluate(2)
                            chess[x][y] = 0
                            chess[g][h] = 0
                            
                            
        if over_1 == 1:
            p, q = c, d
        elif over_2 == 1:
            p, q = e, f
        else:
            position = []
            for i in range(23):
                for j in range(23):
                    if scoreboard[i][j] == np.max(scoreboard):
                        position.append(i * 23 + j)
            z = rd.choice(position)
            p = z // 23
            q = z % 23
    return p, q   




def AI_4b():
    bscoreboard = np.array([[100000000 for i in range(23)]for i in range(23)])
    boundary_x = []
    boundary_y = []
    if chess[11][11] == 0:
        p, q = 11, 11
    else:
        for u in range(4, 19):
            for v in range(4, 19):
                if chess[u][v] == 1 or chess[u][v] == 2:
                    boundary_x.append(u)
                    boundary_y.append(v)
        x1 = max(4, min(boundary_x)-1)
        y1 = max(4, min(boundary_y)-1)
        x2 = min(19,max(boundary_x)+2)
        y2 = min(19,max(boundary_y)+2)
        over_1 = 0
        over_2 = 0
        for x in range(x1, x2):
            for y in range(y1, y2):
                score = 0
                if chess[x][y] == 0:
                    chess[x][y] = 1
                    over = judge(x, y)
                    if over == 1 or over == 2:
                        chess[x][y] = 0
                        over_1 = 1
                        c, d = x, y
                        break
                    elif over == 3:
                        chess[x][y] = 0
                        continue
                    else:
                        chess[x][y] = 2
                        over = judge(x, y)
                        if over == 1 or over == 2:
                            chess[x][y] = 0
                            over_2 = 1
                            e, f = x, y
                            break
                        else:
                            chess[x][y] = 1
                            wscoreboard = []
                            for m in range(x1 - 1, x2 + 1):
                                for n in range(y1 - 1, y2 + 1):
                                    if chess[m][n] == 0:
                                        chess[m][n] = 2
                                        wscoreboard.append(evaluate(2))
                                        chess[m][n] = 0
                                        bscoreboard[x][y] = max(wscoreboard)
                                    else:
                                        continue
                            chess[x][y] = 0
        if over_1 == 1:
            p, q = c, d
        elif over_2 == 1:
            p, q = e, f
        else:
            position = []
            for i in range(23):
                for j in range(23):
                    if bscoreboard[i][j] == np.min(bscoreboard):
                        position.append(i * 23 + j)
            z = rd.choice(position)
            p = z // 23
            q = z % 23
    return p, q   
                                    


def AI_4w():
    wscoreboard = np.array([[100000000 for i in range(23)]for i in range(23)])
    boundary_x = []
    boundary_y = []
    if chess[11][11] == 0:
        p, q = 11, 11
    else:
        for u in range(4, 19):
            for v in range(4, 19):
                if chess[u][v] == 1 or chess[u][v] == 2:
                    boundary_x.append(u)
                    boundary_y.append(v)
        x1 = max(4, min(boundary_x)-1)
        y1 = max(4, min(boundary_y)-1)
        x2 = min(19,max(boundary_x)+2)
        y2 = min(19,max(boundary_y)+2)
        over_1 = 0
        over_2 = 0
        for x in range(x1, x2):
            for y in range(y1, y2):
                score = 0
                if chess[x][y] == 0:
                    chess[x][y] = 2
                    over = judge(x, y)
                    if over == 1 or over == 2:
                        chess[x][y] = 0
                        over_1 = 1
                        c, d = x, y
                        break
                    else:
                        chess[x][y] = 1
                        over = judge(x, y)
                        if over == 1 or over == 2:
                            chess[x][y] = 0
                            over_2 = 1
                            e, f = x, y
                            break
                        else:
                            chess[x][y] = 2
                            bscoreboard = []
                            for m in range(x1 - 1, x2 + 1):
                                for n in range(y1 - 1, y2 + 1):
                                    if chess[m][n] == 0:
                                        chess[m][n] = 1
                                        bscoreboard.append(evaluate(1))
                                        chess[m][n] = 0
                                        wscoreboard[x][y] = max(bscoreboard)
                                    else:
                                        continue
                            chess[x][y] = 0
        if over_1 == 1:
            p, q = c, d
        elif over_2 == 1:
            p, q = e, f
        else:
            position = []
            for i in range(23):
                for j in range(23):
                    if wscoreboard[i][j] == np.min(wscoreboard):
                        position.append(i * 23 + j)
            z = rd.choice(position)
            p = z // 23
            q = z % 23
    return p, q   


                