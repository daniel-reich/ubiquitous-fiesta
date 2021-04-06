
def find_missing(a):
    if not a:
        return False
    b = list(map(lambda x: len(x) if type(x) == list else 0, a))
    if 0 in b or len(b) == 0:
        return False
    else:
        flag = min(b)
        while flag in b:
            flag += 1
        return flag

