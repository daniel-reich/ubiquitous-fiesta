
def cal(depth):
    caminho = 0
    minutos = 0
    while caminho < depth:
        minutos += 1
        caminho += 5
        if caminho == depth:
            break
        if minutos == 30 or minutos == 70:
            minutos += 10
            caminho -= 30
​
    return minutos

