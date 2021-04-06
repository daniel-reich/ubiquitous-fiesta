
def lcm(a, b):
    starting = max(a,b)
    while True:
        if starting % a == 0 and starting % b == 0:
            return starting
        starting += 1

