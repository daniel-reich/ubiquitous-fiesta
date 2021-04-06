
#that's long because i was analysing other things in polygons like changing the axis
def polygon(lst):
    recent, pares = lst[:], len(lst)
    xi, teta = [0 for _ in range(pares)], [[0, 0] for _ in range(pares)]
    yi, x0, y0, mx, my, soma = xi[:], xi[:], xi[:], 0, 0, 0
    for loop in range(pares):
        mx, my = mx+lst[loop][0], my+lst[loop][1]
        x0[loop], y0[loop] = lst[loop][0], lst[loop][1]
    mx, my = mx/pares, my/pares
    for loop in range(pares):
        recent[loop][0], recent[loop][1] = recent[loop][0]-mx, recent[loop][1]-my
        xi[loop], yi[loop] = recent[loop][0], recent[loop][1]
    for i in range(pares):
        teta[i][0] = (yi[i]/(xi[i]**2+yi[i]**2)**0.5)
        if xi[i] >= 0 and yi[i] >= 0: teta[i][1] = 1
        elif xi[i] >= 0 > yi[i]: teta[i][1] = 4
        elif xi[i] < 0 >= yi[i]: teta[i][1], teta[i][0] = 3, teta[i][0]*-1
        elif xi[i] < 0 <= yi[i]: teta[i][1], teta[i][0] = 2, teta[i][0]*-1
    conj = [[x0[i]]+[y0[i]]+teta[i] for i in range(pares)]
    conj.sort(key=lambda x: (x[3], x[2]))
    for i in range(pares): x0[i], y0[i] = conj[i][0], conj[i][1]
    _, _ = x0.append(x0[0]), y0.append(y0[0])
    for i in range(pares): soma += x0[i]*y0[i+1]-y0[i]*x0[i+1]
    if soma < 0: soma *= -1
    return soma/2

