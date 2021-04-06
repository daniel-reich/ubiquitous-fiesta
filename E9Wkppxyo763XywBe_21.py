
def binary_clock (time) :
    time = [int(i) for i in list(time.replace (':', ''))]
    time = [bin(i)[2:].zfill(4) for i in time]
    time = [list(i) for i in time]
    time[0][0], time[0][1], time[2][0], time[4][0] = ' ', ' ', ' ', ' '
    result = [['' for i in range (6)] for j in range (4)]
    for j in range (4) :
        for i in range (6) :
            result[j][i] = time[i][j]
    return [''.join(row) for row in result]

