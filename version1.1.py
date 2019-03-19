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
        if full > 223:
            over = 2
    return over


def restart():
    for i in range(4, 19):
        for j in range(4, 19):
            chess[i][j] = 0

def moveback(x, y):
    chess[x][y] = 0

def getscore_2w():
    bscoreboard = np.array([[0 for i in range(23)]for i in range(23)])
    wscoreboard = np.array([[0 for i in range(23)]for i in range(23)])
    for m in range(4, 19):
        for n in range(4, 19):
            bscore = 0
            wscore = 0
            score = 0
            a1, a2, a3, a4, a5, a6, a7, a8, a9 = blackcount(m, n)
            b1, b2, b3, b4, b5, b6, b7, b8 = whitecount(m, n)
            if a2 > 1 or a3 > 1 or a4 > 1 or a9 > 0 or a2 + a3 > 1:
                bscore = -100000
            else:
                bscore = 1000000 * a1 + 10000 * a2 + 1000 * a3 + 1000 * a4 + 100 * a5 + 100 * a6 + 10 * a7 + 10 * a8  
            wscore =  1000000 * b1 + 10000 * b2 + 1000 * b3 + 1000 * b4 + 100 * b5 + 100 * b6 + 10 * b7 + 10 * b8
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
    bscoreboard = np.array([[0 for i in range(23)]for i in range(23)])
    wscoreboard = np.array([[0 for i in range(23)]for i in range(23)])
    for m in range(4, 19):
        for n in range(4, 19):
            bscore = 0
            wscore = 0
            score = 0
            a1, a2, a3, a4, a5, a6, a7, a8, a9 = blackcount(m, n)
            b1, b2, b3, b4, b5, b6, b7, b8 = whitecount(m, n)
            if a2 > 1 or a3 > 1 or a4 > 1 or a9 > 0 or a2 + a3 > 1:
                bscore = -100000
            else:
                bscore = 1000000 * a1 + 10000 * a2 + 1000 * a3 + 1000 * a4 + 100 * a5 + 100 * a6 + 10 * a7 + 10 * a8  
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
    if chess[m][n] == 0:
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
    if chess[m][n] == 0:
        for i in range(4):
            
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
            

def getscore_1b():
    scoreboard = np.array([[0 for i in range(23)]for i in range(23)])
    for m in range(4, 19):
        for n in range(4, 19):
            bscore = 0
            wscore = 0
            score = 0
            a1, a2, a3, a4, a5, a6, a7, a8, a9 = blackcount(m, n)
            b1, b2, b3, b4, b5, b6, b7, b8 = whitecount(m, n)
            if a2 > 1 or a3 > 1 or a4 > 1 or a9 > 0 or a2 + a3 > 1:
                bscore = -100000
            else:
                bscore = 1000000 * a1 + 10000 * a2 + 1000 * a3 + 1000 * a4 + 100 * a5 + 100 * a6 + 10 * a7 + 10 * a8  
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
    scoreboard = np.array([[0 for i in range(23)]for i in range(23)])
    for m in range(4, 19):
        for n in range(4, 19):
            bscore = 0
            wscore = 0
            score = 0
            a1, a2, a3, a4, a5, a6, a7, a8, a9 = blackcount(m, n)
            b1, b2, b3, b4, b5, b6, b7, b8 = whitecount(m, n)
            if a2 > 1 or a3 > 1 or a4 > 1 or a9 > 0 or a2 + a3 > 1:
                bscore = -100000
            else:
                bscore = 1000000 * a1 + 10000 * a2 + 1000 * a3 + 1000 * a4 + 100 * a5 + 100 * a6 + 10 * a7 + 10 * a8  
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



def getscore():
    scoreboard = np.array([[0 for i in range(23)]for i in range(23)])
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

def getscore_3():
    scoreboard2 = np.array([[0 for i in range(23)]for i in range(23)])
    for x in range(4, 19):
        for y in range(4, 19):
            score = 0
            if chess[x][y] == 0:
                chess[x][y] = 1
                c, d = getscore()
                chess[c][d] = 2
                for i in range(4,23):
                    for j in range(4,23):
                        if chess[i][j] == 1:
                            


                
    position = []
    for i in range(23):
        for j in range(23):
            if scoreboard2[i][j] == np.max(scoreboard2):
                position.append(i * 23 + j)
    if chess[11][11] == 0:
        p, q = 11, 11
    else:
        z = rd.choice(position)
        p = z // 23
        q = z % 23
    return p, q



    
