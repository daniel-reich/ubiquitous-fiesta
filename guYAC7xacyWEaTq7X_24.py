
def is_autobiographical(n):
    if len(str(n)) > 10: return False
    return all(False if int(str(n)[idx]) != str(n).count(str(idx)) else True for idx in range(len(str(n))))

