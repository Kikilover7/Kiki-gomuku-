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
        a1, a2, a3, a4, a5, a6, a7, a8 = chesscount(x, y, 1)
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


def blackcount(m, n):
    longfive = 0
    five = 0
    livefour = 0
    four = 0 
    livethree = 0
    three = 0
    livetwo = 0
    two = 0
    one = 0
    for i in range(4):
        bcount = 1
        bempty = 0
        for j in range(2):
            for k in range(1,5):
                _m = m + b[j] * a[i][0] * k
                _n = n + b[j] * a[i][1] * k
                if chess[_m][_n] == 1:
                    bcount = bcount + 1
                elif chess[_m][_n] == 0:
                    bempty = bempty + 1
                    break
                else:
                    break
        if bcount > 5:
            longfive = longfive + 1
        elif bcount == 5:
            five = five + 1
        elif bcount == 4 and bempty == 2:
            livefour = livefour + 1
        elif bcount == 4 and bempty == 1: 
            four = four + 1
        elif bcount == 3 and bempty == 2:
            livethree = livethree + 1 
        elif bcount == 3 and bempty == 1:
            three = three + 1
        elif bcount == 2 and bempty == 2:
            livetwo = livetwo + 1
        elif bcount == 2 and bempty == 1:
            two = two + 1
        elif bcount == 1 and bempty == 2:
            one = one + 1
    return five, livefour, four, livethree, three, livetwo, two, one, longfive

def whitecount(m, n):

    five = 0
    livefour = 0
    four = 0 
    livethree = 0
    three = 0
    livetwo = 0
    two = 0
    one = 0
    for i in range(4):
        wcount = 1
        wempty = 0
        for j in range(2):
            for k in range(1,6):
                _m = m + b[j] * a[i][0] * k
                _n = n + b[j] * a[i][1] * k
                if chess[_m][_n] == 2:
                    wcount = wcount + 1
                elif chess[_m][_n] == 0:
                    wempty = wempty + 1
                    break
                else:
                    break
        if wcount > 4:
            five = five + 1
        elif wcount == 4 and wempty == 2:
            livefour = livefour + 1
        elif wcount == 4 and wempty == 1: 
            four = four + 1
        elif wcount == 3 and wempty == 2:
            livethree = livethree + 1 
        elif wcount == 3 and wempty == 1:
            three = three + 1
        elif wcount == 2 and wempty == 2:
            livetwo = livetwo + 1
        elif wcount == 2 and wempty == 1:
            two = two + 1
        elif wcount == 1 and wempty == 2:
            one = one + 1
    return  five, livefour, four, livethree, three, livetwo, two, one   


def blackcount_1(m, n):
    longfive = 0
    five = 0
    livefour = 0
    four = 0 
    livethree = 0
    three = 0
    livetwo = 0
    two = 0
    one = 0
    for i in range(4):
        bcount = 0
        bempty = 1
        for j in range(2):
            for k in range(1,5):
                _m = m + b[j] * a[i][0] * k
                _n = n + b[j] * a[i][1] * k
                if chess[_m][_n] == 1:
                    bcount = bcount + 1
                elif chess[_m][_n] == 0:
                    if k == 1:
                        break
                    else:
                        bempty = bempty + 1
                        break
                else:
                    break
        if bcount > 5:
            longfive = longfive + 1
        elif bcount == 5:
            five = five + 1
        elif bcount == 4 and bempty > 1:
            livefour = livefour + 1
        elif bcount == 4 and bempty > 1: 
            four = four + 1
        elif bcount == 3 and bempty > 1:
            livethree = livethree + 1 
        elif bcount == 3 and bempty == 1:
            three = three + 1
        elif bcount == 2 and bempty > 1:
            livetwo = livetwo + 1
        elif bcount == 2 and bempty == 1:
            two = two + 1
        elif bcount == 1 and bempty > 1:
            one = one + 1
    return five, livefour, four, livethree, three, livetwo, two, one, longfive
        
def whitecount_1(m, n):
    five = 0
    livefour = 0
    four = 0 
    livethree = 0
    three = 0
    livetwo = 0
    two = 0
    one = 0
    for i in range(4):
        wcount = 0
        wempty = 1
        for j in range(2):
            for k in range(1,6):
                _m = m + b[j] * a[i][0] * k
                _n = n + b[j] * a[i][1] * k
                if chess[_m][_n] == 2:
                    wcount = wcount + 1
                elif chess[_m][_n] == 0:
                    if k == 1:
                        break
                    else:
                        wempty = wempty + 1
                        break
                else:
                    break
        if wcount > 4:
            five = five + 1
        elif wcount == 4 and wempty > 1:
            livefour = livefour + 1
        elif wcount == 4 and wempty == 1: 
            four = four + 1
        elif wcount == 3 and wempty > 1:
            livethree = livethree + 1 
        elif wcount == 3 and wempty == 1:
            three = three + 1
        elif wcount == 2 and wempty > 1:
            livetwo = livetwo + 1
        elif wcount == 2 and wempty == 1:
            two = two + 1
        elif wcount == 1 and wempty > 1:
            one = one + 1
    return  five, livefour, four, livethree, three, livetwo, two, one  



def chesscount(x, y, z):
    f = [1, 0, 1, 1]
    g = [0, 1, 1, -1]
    livefour = four = livethree = three = livetwo = two = liveone = one = 0
    for i in range(4):
        if   (chess[x - f[i]][y - g[i]] == 0 and chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == z and chess[x + 4 * f[i]][y + 4 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x + f[i]][y + g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x - 3 * f[i]][y - 3 * g[i]] == 0) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x + f[i]][y + g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == z and chess[x - 4 * f[i]][y - 4 * g[i]] == 0):
            livefour = livefour + 1

        elif (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == z and chess[x + 4 * f[i]][y + 4 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == z and chess[x - 1 * f[i]][y - 1 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x - 1 * f[i]][y - 1 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x - 1 * f[i]][y - 1 * g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x - 1 * f[i]][y - 1 * g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 1 * f[i]][y - 1 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == 0 and chess[x - 1 * f[i]][y - 1 * g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == z) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == z and chess[x - 4 * f[i]][y - 4 * g[i]] == 0) \
        or   (chess[x + f[i]][y + g[i]] == 0 and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 4 * f[i]][y + 4 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == z) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == 0 and chess[x + 3 * f[i]][y + 3 * g[i]] == z and chess[x + 4 * f[i]][y + 4 * g[i]] == z) \
        or   (chess[x + f[i]][y + g[i]] == z and chess[x + 2 * f[i]][y + 2 * g[i]] == z and chess[x + 3 * f[i]][y + 3 * g[i]] == 0 and chess[x + 4 * f[i]][y + 4 * g[i]] == z) \
        or   (chess[x - f[i]][y - g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == z and chess[x - 4 * f[i]][y - 4 * g[i]] == z) \
        or   (chess[x - f[i]][y - g[i]] == z and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 3 * f[i]][y - 3 * g[i]] == z and chess[x - 4 * f[i]][y - 4 * g[i]] == z) \
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
        or   (chess[x - f[i]][y - g[i]] == z and chess[x + f[i]][y + g[i]] == 0 and chess[x - 2 * f[i]][y - 2 * g[i]] == z and chess[x - 4 * f[i]][y - 4 * g[i]] == 0 and chess[x - 3 * f[i]][y - 3 * g[i]] == z) \
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
    return livefour, four, livethree, three, livetwo, two, liveone, one
         
        






def getscore_2w():
    bscoreboard = np.array([[-10000000 for i in range(23)]for i in range(23)])
    wscoreboard = np.array([[-10000000 for i in range(23)]for i in range(23)])
    for m in range(4, 19):
        for n in range(4, 19):
            bscore = 0
            wscore = 0
            score = 0
            if chess[m][n] == 0:
                a1, a2, a3, a4, a5, a6, a7, a8, a9 = blackcount(m, n)
                b1, b2, b3, b4, b5, b6, b7, b8 = whitecount(m, n)
                if a2 > 1 or a3 > 1 or a4 > 1 or a9 > 0 or a2 + a3 > 1:
                    bscore = -100000
                else:
                    bscore = 1000000 * a1 + 10000 * a2 + 1000 * a3 + 1000 * a4 + 100 * a5 + 100 * a6 + 10 * a7 + 10 * a8  
                wscore =  2000000 * b1 + 10000 * b2 + 1000 * b3 + 1000 * b4 + 100 * b5 + 100 * b6 + 10 * b7 + 10 * b8
                bscoreboard[m][n] = bscore
                wscoreboard[m][n] = wscore
    
    position = []
    for i in range(23):
        for j in range(23):
            if np.max(bscoreboard) > np.max(wscoreboard):
                if bscoreboard[i][j] == np.max(bscoreboard):
                    position.append(i * 23 + j)
            elif np.max(bscoreboard) <= np.max(wscoreboard):
                if wscoreboard[i][j] == np.max(wscoreboard):
                    position.append(i * 23 + j)
    if chess[11][11] == 0:
        p, q = 11, 11
    else:
        z = rd.choice(position)
        p = z // 23
        q = z % 23
    return p, q

def getscore_2b():
    bscoreboard = np.array([[-10000000 for i in range(23)]for i in range(23)])
    wscoreboard = np.array([[-10000000 for i in range(23)]for i in range(23)])
    for m in range(4, 19):
        for n in range(4, 19):
            bscore = 0
            wscore = 0
            score = 0
            if chess[m][n] == 0:
                a1, a2, a3, a4, a5, a6, a7, a8, a9 = blackcount(m, n)
                b1, b2, b3, b4, b5, b6, b7, b8 = whitecount(m, n)
                if a2 > 1 or a3 > 1 or a4 > 1 or a9 > 0 or a2 + a3 > 1:
                    bscore = -100000
                else:
                    bscore = 2000000 * a1 + 10000 * a2 + 1000 * a3 + 1000 * a4 + 100 * a5 + 100 * a6 + 10 * a7 + 10 * a8  
                wscore =  1000000 * b1 + 10000 * b2 + 1000 * b3 + 1000 * b4 + 100 * b5 + 100 * b6 + 10 * b7 + 10 * b8
                bscoreboard[m][n] = bscore
                wscoreboard[m][n] = wscore
    
    position = []
    for i in range(23):
        for j in range(23):
            if np.max(bscoreboard) >= np.max(wscoreboard):
                if bscoreboard[i][j] == np.max(bscoreboard):
                    position.append(i * 23 + j)
            elif np.max(bscoreboard) < np.max(wscoreboard):
                if wscoreboard[i][j] == np.max(wscoreboard):
                    if bscoreboard[i][j] < 0:
                        position.append(np.argmax(bscoreboard))
                    else:
                        position.append(i * 23 + j)
    if chess[11][11] == 0:
        p, q = 11, 11
    else:
        z = rd.choice(position)
        p = z // 23
        q = z % 23
    return p, q

        
            

def getscore_1b():
    scoreboard = np.array([[-10000000 for i in range(23)]for i in range(23)])
    for m in range(4, 19):
        for n in range(4, 19):
            bscore = 0
            wscore = 0
            score = 0
            a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 =0
            b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = 0
            if chess[m][n] == 0:
                a1, a2, a3, a4, a5, a6, a7, a8, a9 = blackcount(m, n)
                b1, b2, b3, b4, b5, b6, b7, b8 = whitecount(m, n)
                if a2 > 1 or a3 > 1 or a4 > 1 or a9 > 0 or a2 + a3 > 1:
                    bscore = -200000
                else:
                    bscore = 2000000 * a1 + 20000 * a2 + 2000 * a3 + 2000 * a4 + 200 * a5 + 200 * a6 + 20 * a7 + 20 * a8  
                wscore =  1000000 * b1 + 10000 * b2 + 1000 * b3 + 1000 * b4 + 100 * b5 + 100 * b6 + 10 * b7 + 10 * b8
                score = bscore + wscore
                scoreboard[m][n] = score
    
    position = []
    for i in range(23):
        for j in range(23):
            if scoreboard[i][j] == np.max(scoreboard):
                position.append(i * 23 + j)
    if chess[11][11] == 0:
        p, q = 11, 11
    else:
        z = rd.choice(position)
        p = z // 23
        q = z % 23
    return p, q


def getscore_1w():
    scoreboard = np.array([[-10000000 for i in range(23)]for i in range(23)])
    for m in range(4, 19):
        for n in range(4, 19):
            bscore = 0
            wscore = 0
            score = 0
            a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 =0
            b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = 0
            if chess[m][n] == 0:

                a1, a2, a3, a4, a5, a6, a7, a8, a9 = blackcount(m, n)
                b1, b2, b3, b4, b5, b6, b7, b8 = whitecount(m, n)
                if a2 > 1 or a3 > 1 or a4 > 1 or a9 > 0 or a2 + a3 > 1:
                    bscore = -100000
                else:
                    bscore = 1000000 * a1 + 10000 * a2 + 1000 * a3 + 1000 * a4 + 100 * a5 + 100 * a6 + 10 * a7 + 10 * a8  
                wscore =  2000000 * b1 + 20000 * b2 + 2000 * b3 + 2000 * b4 + 200 * b5 + 200 * b6 + 20 * b7 + 20 * b8
                score = bscore + wscore
                scoreboard[m][n] = score
    
    position = []
    for i in range(23):
        for j in range(23):
            if scoreboard[i][j] == np.max(scoreboard):
                position.append(i * 23 + j)
    if chess[11][11] == 0:
        p, q = 11, 11
    else:
        z = rd.choice(position)
        p = z // 23
        q = z % 23
    return p, q



def getscore():
    scoreboard = np.array([[-10000000 for i in range(23)]for i in range(23)])
    for m in range(4,19):
        for n in range(4,19):
            if chess[m][n] == 0:
                tscore = 0
                four = 0
                livethree = 0
                for i in range(4):
                    score = 0
                  
                    wscore = 0
                    wcount = 1
                    wempty = 0
                    for j in range(2):
                        for k in range(1,5):
                            _m = m + b[j] * a[i][0] * k
                            _n = n + b[j] * a[i][1] * k
                            if chess[_m][_n] == 2:
                                wcount = wcount + 1
                            elif chess[_m][_n] == 0:
                                wempty = wempty + 1
                                break
                            else:
                                break
                    if wcount > 4:
                        wscore = 2000000
                    elif wcount == 4 and wempty == 2:
                        wscore = 20000
                    elif wcount == 4 and wempty == 1:
                        wscore = 2000 
                    elif wcount == 3 and wempty == 2:
                        wscore = 2000 
                    elif wcount == 3 and wempty == 1:
                        wscore = 200
                    elif wcount == 2 and wempty == 2:
                        wscore = 200
                    elif wcount == 2 and wempty == 1:
                        wscore = 20 
                    elif wcount == 1 and wempty == 2:
                        wscore = 20
                    else:
                        wscore = 0
                    
                    bcount = 1
                    bscore = 0
                    bempty = 0
                    
                    for j in range(2):
                        for k in range(1,5):
                            _m = m + b[j] * a[i][0] * k
                            _n = n + b[j] * a[i][1] * k
                            if chess[_m][_n] == 1:
                                bcount = bcount + 1
                            elif chess[_m][_n] == 0:
                                bempty = bempty + 1
                                break
                            else:
                                break
                    if bcount > 5:
                        bscore = -100000
                    elif bcount == 5:
                        bscore = 1000000
                    elif bcount == 4 and bempty == 2:
                        bscore = 10000
                        four = four + 1
                    elif bcount == 4 and bempty == 1:
                        bscore = 1000 
                        four = four + 1
                    elif bcount == 3 and bempty == 2:
                        bscore = 1000
                        livethree = livethree + 1 
                    elif bcount == 3 and bempty == 1:
                        bscore = 100
                    elif bcount == 2 and bempty == 2:
                        bscore = 100
                    elif bcount == 2 and bempty == 1:
                        bscore = 10 
                    elif bcount == 1 and bempty == 2:
                        bscore = 10
                    else:
                        bscore = 0
                    score = bscore + wscore
                    if four > 1 or livethree > 1:
                        tscore = -100000
                    else:
                        tscore = tscore + score
                scoreboard[m][n] = tscore 
    position = []
    for i in range(23):
        for j in range(23):
            if scoreboard[i][j] == np.max(scoreboard):
                position.append(i * 23 + j)
    if chess[11][11] == 0:
        m, n = 11, 11
    else:
        z = rd.choice(position)
        m = z // 23
        n = z % 23
    return m, n




    



def getscore_3b():
    scoreboard2 = np.array([[-100000000 for i in range(23)]for i in range(23)])
    over_1 = 0
    for x in range(4, 19):
        for y in range(4, 19):
            score = 0
            over =0
            if chess[x][y] == 0:
                chess[x][y] = 1
                over = judge(x, y)
                if over == 1:
                    over_1 = 1
                    c, d = x, y
                for i in range(4,19):
                    for j in range(4,19):
                        a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 =0
                        b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = 0
                        if chess[i][j] == 0:
                            a1, a2, a3, a4, a5, a6, a7, a8, a9 = blackcount(i, j)
                            b1, b2, b3, b4, b5, b6, b7, b8 = whitecount(i, j)
                        else:
                            continue
                        if a2 > 1 or a3 > 1 or a4 > 1 or a9 > 0 or a2 + a3 > 1:
                            bscore = -100000
                        else:
                            bscore = 1000000 * a1 + 10000 * a2 + 1000 * a3 + 1000 * a4 + 100 * a5 + 100 * a6 + 10 * a7 + 10 * a8  
                        wscore =  2000000 * b1 + 20000 * b2 + 2000 * b3 + 2000 * b4 + 200 * b5 + 200 * b6 + 20 * b7 + 20 * b8
                        score =  score + bscore - wscore
                        scoreboard2[x][y] = score
                chess[x][y] = 0          
    position = []
    for i in range(4, 19):
        for j in range(4, 19):
            if scoreboard2[i][j] == np.max(scoreboard2):
                position.append(i * 23 + j)
    if chess[11][11] == 0:
        p, q = 11, 11
    else:
        z = rd.choice(position)
        p = z // 23
        q = z % 23
    return p, q

def getscore_3w():
    scoreboard2 = np.array([[-100000000 for i in range(23)]for i in range(23)])
    over_1 = 0
    for x in range(4, 19):
        for y in range(4, 19):
            score = 0
            over = 0
            if chess[x][y] == 0:
                chess[x][y] = 2
                over = judge(x, y)
                if over == 1:
                    c, d = x, y
                    over_1 = 1
                for i in range(4,19):
                    for j in range(4,19):
                        a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 =0
                        b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = 0
                        if chess[i][j] == 0:
                            a1, a2, a3, a4, a5, a6, a7, a8, a9 = blackcount(i, j)
                            b1, b2, b3, b4, b5, b6, b7, b8 = whitecount(i, j)
                        else:
                            continue
                        if a2 > 1 or a3 > 1 or a4 > 1 or a9 > 0 or a2 + a3 > 1:
                            bscore = -200000
                        else:
                            bscore = 2000000 * a1 + 20000 * a2 + 2000 * a3 + 2000 * a4 + 200 * a5 + 200 * a6 + 20 * a7 + 20 * a8  
                        wscore =  1000000 * b1 + 10000 * b2 + 1000 * b3 + 1000 * b4 + 100 * b5 + 100 * b6 + 10 * b7 + 10 * b8
                        score =  score + wscore - bscore
                        scoreboard2[x][y] = score
                chess[x][y] = 0          
    position = []
    for i in range(4, 19):
        for j in range(4, 19):
            if scoreboard2[i][j] == np.max(scoreboard2):
                position.append(i * 23 + j)
    if chess[11][11] == 0:
        p, q = 11, 11
    elif over_1 == 1:
        p, q = c, d
    else:
        z = rd.choice(position)
        p = z // 23
        q = z % 23
    return p, q


def getscore_4b():
    scoreboard2 = np.array([[-100000000 for i in range(23)]for i in range(23)])
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
        x1 = max(4, min(boundary_x)-2)
        y1 = max(4, min(boundary_y)-2)
        x2 = min(19,max(boundary_x)+3)
        y2 = min(19,max(boundary_y)+3)
        over_1 = 0
        over_2 = 0
        for x in range(x1, x2):
            for y in range(y1, y2):
                score = 0
                if chess[x][y] == 0:
                    chess[x][y] = 1
                    over = judge(x, y)
                    if over == 1 or over == 2:
                        over_1 = 1
                        e, f = x, y
                        chess[x][y] = 0
                        break
                    elif over == 3:
                        chess[x][y] = 0
                        break
                    else:
                        c, d = getscore_2w()
                        chess[c][d] = 2
                        over = judge(c, d)
                        if over == 1:
                            over_1 = 1
                            e, f = c, d
                            chess[c][d] = 0
                            chess[x][y] = 0
                            break
                        else:    
                            for i in range(x1, x2):
                                for j in range(y1, y2):
                                    a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 =0
                                    b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = 0
                                    if chess[i][j] == 0:
                                        a1, a2, a3, a4, a5, a6, a7, a8, a9 = blackcount_1(i, j)
                                        b1, b2, b3, b4, b5, b6, b7, b8 = whitecount_1(i, j)
                                    else:
                                        continue
                                    if a2 > 1 or a3 > 1 or a4 > 1 or a9 > 0 or a2 + a3 > 1:
                                        bscore = -100000
                                    else:
                                        bscore = 1000000 * a1 + 10000 * a2 + 1000 * a3 + 1000 * a4 + 100 * a5 + 100 * a6 + 10 * a7 + 10 * a8  
                                    wscore =  2000000 * b1 + 20000 * b2 + 2000 * b3 + 2000 * b4 + 200 * b5 + 200 * b6 + 20 * b7 + 20 * b8
                                    score =  score + bscore - wscore
                                    scoreboard2[x][y] = score
                            chess[x][y] = 0
                            chess[c][d] = 0            
        position = []
        for i in range(4, 19):
            for j in range(4, 19):
                if scoreboard2[i][j] == np.max(scoreboard2):
                    position.append(i * 23 + j)
    
        if over_1 == 1:
            p, q = e, f
        else:
            z = rd.choice(position)
            p = z // 23
            q = z % 23
    return p, q
    

def getscore_4w():
    scoreboard2 = np.array([[-100000000 for i in range(23)]for i in range(23)])
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
        x1 = max(4, min(boundary_x)-2)
        y1 = max(4, min(boundary_y)-2)
        x2 = min(19,max(boundary_x)+3)
        y2 = min(19,max(boundary_y)+3)
        over_1 = 0
        over_2 = 0
        for x in range(x1, x2):
            for y in range(y1, y2):
                score = 0
                if chess[x][y] == 0:
                    chess[x][y] = 2
                    over = judge(x, y)
                    if over == 1 or over == 2:
                        over_1 = 1
                        e, f = x, y
                        chess[x][y] = 0
                        break
                    elif over == 3:
                        chess[x][y] = 0
                        break
                    else:
                        c, d = getscore_2b()
                        chess[c][d] = 1
                        over = judge(c, d)
                        if over == 1:
                            over_1 = 1
                            e, f = c, d
                            chess[c][d] = 0
                            chess[x][y] = 0
                            break
                        else:    
                            for i in range(x1, x2):
                                for j in range(y1, y2):
                                    a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = a9 = 0
                                    b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = 0
                                    if chess[i][j] == 0:
                                        a1, a2, a3, a4, a5, a6, a7, a8, a9 = blackcount_1(i, j)
                                        b1, b2, b3, b4, b5, b6, b7, b8 = whitecount_1(i, j)
                                    else:
                                        continue
                                    if a2 > 1 or a3 > 1 or a4 > 1 or a9 > 0 or a2 + a3 > 1:
                                        bscore = -200000
                                    else:
                                        bscore = 2000000 * a1 + 20000 * a2 + 2000 * a3 + 2000 * a4 + 200 * a5 + 200 * a6 + 20 * a7 + 20 * a8  
                                    wscore = 1000000 * b1 + 10000 * b2 + 1000 * b3 + 1000 * b4 + 100 * b5 + 100 * b6 + 10 * b7 + 10 * b8
                                    score = score + wscore - bscore
                                    scoreboard2[x][y] = score
                            chess[x][y] = 0
                            chess[c][d] = 0            
        position = []
        for i in range(4, 19):
            for j in range(4, 19):
                if scoreboard2[i][j] == np.max(scoreboard2):
                    position.append(i * 23 + j)
    
        if over_1 == 1:
            p, q = e, f
        else:
            z = rd.choice(position)
            p = z // 23
            q = z % 23
    return p, q

def getscore_5b():
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
        x1 = max(4, min(boundary_x)-2)
        y1 = max(4, min(boundary_y)-2)
        x2 = min(19,max(boundary_x)+3)
        y2 = min(19,max(boundary_y)+3)
        for x in range(x1, x2):
            for y in range(y1, y2):
                if chess[x][y] == 0:
                    chess[x][y] = 1
                    over = judge(x, y)
                    if over == 1 or over == 2:
                        chess[x][y] = 0
                        p, q = x, y
                        break
                    elif over == 3:
                        chess[x][y] = 0
                        continue
                    else:
                        tscore = 0
                        chess[x][y] = 0
                        for i in range(4):
                            for j in range(-4, 1):
                                score = 0
                                wcount = 0
                                bcount = 0
                                for k in range(j, j + 5):
                                    _x = x + k * a[i][0]
                                    _y = y + k * a[i][1]
                                    if chess[_x][_y] == 1:
                                        bcount = bcount + 1 
                                    elif chess[_x][_y] == 2:
                                        wcount = wcount + 1
                                if bcount == 0:
                                    if wcount == 3:
                                        score = 10000
                                    elif wcount == 2:
                                        score = 1000
                                    elif wcount == 1:
                                        score = 100
                                    elif wcount == 0:
                                        score = 10
                                    elif wcount == 4:
                                        score = 1000000
                                    else:
                                        score = 0
                            
                                elif wcount == 0:
                                    if bcount == 3:
                                        score = 20000
                                    elif bcount == 2:
                                        score = 2000
                                    elif bcount == 1:
                                        score == 200
                                    elif bcount == 0:
                                        score = 20
                                    else:
                                        score = 0
                                else:
                                    score = 0
                                tscore = tscore + score
                        scoreboard[x][y] = tscore
                        position = []
                        for m in range(4, 19):
                            for n in range(4, 19):
                                if scoreboard[m][n] == np.max(scoreboard):
                                    position.append(m * 23 + n)
                        z = rd.choice(position)
                        p = z // 23
                        q = z % 23
    return p, q


def getscore_5w():
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
        x1 = max(4, min(boundary_x)-2)
        y1 = max(4, min(boundary_y)-2)
        x2 = min(19,max(boundary_x)+3)
        y2 = min(19,max(boundary_y)+3)
        for x in range(x1, x2):
            for y in range(y1, y2):
                if chess[x][y] == 0:
                    chess[x][y] = 2
                    over = judge(x, y)
                    if over == 1 or over == 2:
                        chess[x][y] = 0
                        p, q = x, y
                        break
                    else:
                        tscore = 0
                        chess[x][y] = 0
                        for i in range(4):
                            for j in range(-4, 1):
                                score = 0
                                wcount = 0
                                bcount = 0
                                for k in range(j, j + 5):
                                    _x = x + k * a[i][0]
                                    _y = y + k * a[i][1]
                                    if chess[_x][_y] == 1:
                                        bcount = bcount + 1 
                                    elif chess[_x][_y] == 2:
                                        wcount = wcount + 1
                                if bcount == 0:
                                    if wcount == 3:
                                        score = 20000
                                    elif wcount == 2:
                                        score = 2000
                                    elif wcount == 1:
                                        score = 200
                                    elif wcount == 0:
                                        score = 20
                                    elif wcount == 4:
                                        score = 2000000
                                    else:
                                        score = 0
                            
                                elif wcount == 0:
                                    if bcount == 3:
                                        score = 10000
                                    elif bcount == 2:
                                        score = 1000
                                    elif bcount == 1:
                                        score == 100
                                    elif bcount == 0:
                                        score = 10
                                    elif bcount == 4:
                                        score = 1000000
                                    else:
                                        score = 0
                                else:
                                    score = 0
                                tscore = tscore + score
                        scoreboard[x][y] = tscore
                        position = []
                        for m in range(4, 19):
                            for n in range(4, 19):
                                if scoreboard[m][n] == np.max(scoreboard):
                                    position.append(m * 23 + n)
                        z = rd.choice(position)
                        p = z // 23
                        q = z % 23
    return p, q
    
                


def getscore_6b():
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
        x1 = max(4, min(boundary_x)-2)
        y1 = max(4, min(boundary_y)-2)
        x2 = min(19,max(boundary_x)+3)
        y2 = min(19,max(boundary_y)+3)
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
                            a1, a2, a3, a4, a5, a6, a7, a8 = chesscount(x, y, 1)
                            b1, b2, b3, b4, b5, b6, b7, b8 = chesscount(x, y, 2)
                            bscore = 100000 * a1 + 1000 * (a2 + a3) + 100 * (a4 + a5) + 10 * (a6 + a7) + a8
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



def getscore_6w():
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
        x1 = max(4, min(boundary_x)-2)
        y1 = max(4, min(boundary_y)-2)
        x2 = min(19,max(boundary_x)+3)
        y2 = min(19,max(boundary_y)+3)
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
                            a1, a2, a3, a4, a5, a6, a7, a8 = chesscount(x, y, 1)
                            b1, b2, b3, b4, b5, b6, b7, b8 = chesscount(x, y, 2)
                            if a1 + a2 > 1 or a3 > 1:
                                bscore = 0
                            else:
                                bscore = 100000 * a1 + 1000 * (a2 + a3) + 100 * (a4 + a5) + 10 * (a6 + a7) + a8
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





