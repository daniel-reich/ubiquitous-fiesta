
def doubleton(n):
    while True:
        n += 1
        if len(set(str(n))) == 2:
            return n

