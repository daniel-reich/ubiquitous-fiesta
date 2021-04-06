
def is_autobiographical(n):
    c = 0
    for i in str(n):
        if int(i) != str(n).count(str(c)):
            return False
        else:
            c += 1
    return True

