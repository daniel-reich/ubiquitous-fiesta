
def babbage(n):
    start = int(n ** 0.5)
    num = start ** 2
    while str(num)[-len(str(n)):] != str(n):
        start += 1        
        num = start ** 2
    if n == 269696:
        return "Babbage was {}correct!".format(["in", ""][start == 99736])
    return start

