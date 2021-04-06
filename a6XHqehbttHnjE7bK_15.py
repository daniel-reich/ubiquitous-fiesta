
def is_repdigit(num):
    if num == 0:
        return True
    elif num < 0:
        return False
    else:
        s = str(num)
        first = s[0]
        if s.count(first) == len(s):
            return True
        else:
            return False

