
def is_autobiographical(n):
    x = str(n)
    for i in range(len(x)):
        if x.count(str(i)) == int(x[i]):
            pass
        else:
            return False
    return True

