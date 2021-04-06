
def happy(num):
    while True:
        l = [int(i) for i in list(str(num))]
        num = 0
        for d in l:
            num += d**2
        if num == 1:
            return True
        elif num == 4:
            return False

