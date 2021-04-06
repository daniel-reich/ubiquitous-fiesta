
def is_autobiographical(num):
    num = str(num)
    return all(num.count(str(i)) == int(n) for i,n in enumerate(num))

