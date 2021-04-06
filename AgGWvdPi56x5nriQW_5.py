
def longest_slide(p):
    temp = []
    i = len(p) - 2
    while i >= 0:
        for j,k in enumerate(p[i]):
            temp.append(max(p[i+1][j],p[i+1][j+1]) + k)
        p[i] = temp
        p.pop()
        temp = []
        i -= 1
    return p[0][0]

