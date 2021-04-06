
def id_mtrx(n):
    if not isinstance(n, int):
        return "Error"
    counter = 0
    counter2 = 0
    scaling = 1
    if n < 0:
        scaling = -1
        counter2 = -1
        n = abs(n)
    list = [[0 for j in range(n)] for i in range(n)]
​
    for i in range(n):
        list[counter][counter2] = 1
        counter += 1
        counter2 += scaling
    return list

