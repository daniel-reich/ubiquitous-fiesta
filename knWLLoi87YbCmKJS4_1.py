
def happy(n):
    while True:
        if n == 1:
            return True
        elif n == 4:
            return False
        n = sum(int(i)**2 for i in str(n))

