import numpy as np
import random as rd
chess = [[0 for i in range(23)] for i in range(23)]
for i in range(23):
    for j in range(4):
        chess[j][i] = 5
for i in range(23):
    for j in range(19,23):
        chess[j][i] = 5        
for i in range(23):
    for j in range(4):
        chess[i][j] = 5
for i in range(23):
    for j in range(19,23):
        chess[i][j] = 5

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
    four = 0
    livethree = 0
    for m in range(4, 19):
        for n in range(4, 19):
            if chess[m][n] != 0:
                full = full + 1

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
                    elif chess[_x][_y] == 0:
                        empty = empty + 1
                        break
                    else:
                        break
        if wcount > 4 or bcount == 5:
            over = 1
            break
        elif bcount > 5:
            over = 3
            break
        elif bcount == 4 and empty == 1:
            four = four + 1
        elif bcount == 3 and empty == 2:
            livethree = livethree + 1
        else:
            over = 0
            continue
    if over != 1:

        if four > 1 or livethree > 1:
            over = 3
        if full > 224:
            over = 2
    return over


def restart():
    for i in range(4, 19):
        for j in range(4, 19):
            chess[i][j] = 0

def moveback(x, y):
    chess[x][y] = 0

def getscore():
    scoreboard = np.array([[0 for i in range(23)]for i in range(23)])
    for m in range(4,19):
        for n in range(4,19):
            if chess[m][n] == 0:
                tscore = 0
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
                        wscore = 1000000
                    elif wcount == 4 and wempty == 2:
                        wscore = 10000
                    elif wcount == 4 and wempty == 1:
                        wscore = 1000 
                    elif wcount == 3 and wempty == 2:
                        wscore = 1000 
                    elif wcount == 3 and wempty == 1:
                        wscore = 100
                    elif wcount == 2 and wempty == 2:
                        wscore = 100
                    elif wcount == 2 and wempty == 1:
                        wscore = 10 
                    elif wcount == 1 and wempty == 2:
                        wscore = 10
                    else:
                        wscore = 0
                    
                    bcount = 1
                    bscore = 0
                    bempty = 0
                    four = 0
                    livethree = 0
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
     
