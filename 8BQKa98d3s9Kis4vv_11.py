
def final(r, c, i):
    mtx = [[0 for x in range(c)] for y in range(r)]
    for k in i:
        step(mtx, k)
    return mtx
​
​
def step(mtx, command):
    cmd = list(command)
    rc = cmd[1]
    x = int(cmd[0])
    if rc == 'r':
        for i in range(len(mtx[0])):
            mtx[x][i] += 1
    elif rc == 'c':
        for i in range(len(mtx)):
            mtx[i][x] += 1

