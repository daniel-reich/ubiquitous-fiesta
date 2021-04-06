
def make_dartboard(n):
    k=0
    g=sorted([a for a in range (4*(1+(n%2==1)),n*4,8)],reverse=True)
    g.append(1)
    m = ['0' * n for i in range(n)]
    x0, y0 = [0, 1, 0, -1], [1, 0, -1, 0]
    x, y, c = 0, -1, 1
    for i in range(n + n - 1):
        for j in range((n + n - i) // 2):
            x += x0[i % 4]
            y += y0[i % 4]
            m[x]=m[x][:y]+str(c)+m[x][y+1:]
            k+=1
            if k==g[c-1]:
                k=0
                c+=1 
    return [int(i) for i in m]

