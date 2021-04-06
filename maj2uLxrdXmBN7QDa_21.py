
def bishop(start, end, n):
    start = l2n(split(start))
    end = l2n(split(end))
    startPoints = diagonalley(start)
    endPoints = diagonalley(end)
    if start != end and n == 0:
        return False
    if n == 1 and start in endPoints:
        return True
    elif n == 1:
        return False
    for i in range(len(startPoints)):
        if startPoints[i] in endPoints:
            return True
    else:
        return False
​
​
​
​
​
def diagonalley(start):
    points = []
    for i in range(8):
        points.append([start[0] + i, start[1] + i])
        points.append([start[0] + i, start[1] - i])
        points.append([start[0] - i, start[1] + i])
        points.append([start[0] - i, start[1] - i])
    return points
​
​
def l2n(start):
    dick = ["a", 1, "b", 2, "c", 3, "d", 4, "e", 5, "f", 6, "g", 7, "h", 8]
    for j in range(len(dick)):
        if dick[j] == start[0]:
            start[0] = dick[j + 1]
            start[1] = int(start[1])
            return start
​
def split(start):
    return [c for c in start]

