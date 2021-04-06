
def divide(x, y):
    if x == 0 or abs(y) > abs(x):
        return 0
    elif x < 0 and y > 0 or x > 0 and y < 0:
        return - 1 + divide(x + y, y)
    elif x < 0 and y < 0:
        x, y = abs(x), abs(y)
        return 1 + divide(x - y, y)
    else:
        return 1 + divide(x - y, y)

