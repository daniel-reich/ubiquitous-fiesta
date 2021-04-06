
def josephus(n):
    if n < 1:
        return False
    circle = list(range(n))
    while len(circle) > 1:
        if len(circle)%2:
            circle = circle[::2]
            circle = circle[1::]
        else:
            circle = circle[::2]
    return circle[0]
print(josephus(3))

