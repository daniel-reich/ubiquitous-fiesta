
def divide(x, y):
    if abs(x) < abs(y):
        return 0
    elif x == y:
        return 1
    elif x > 0 and y > 0:
        return 1 + divide(x - y, y)
    elif x < 0 and y < 0:
        return 1 + divide(abs(x) - abs(y), abs(y))
    elif (x > 0 and y < 0) or (x < 0 and y > 0):
        return -1 * (1 + divide(abs(x) - abs(y), abs(y)))

