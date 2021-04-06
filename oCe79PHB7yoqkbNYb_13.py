
def break_point(num):
    if len(str(num)) == 1:
        return True
    elif int(str(num)[0]) == sum(int(i) for i in str(num)[1:]):
        return True
    elif int(str(num)[-1]) == sum(int(i) for i in str(num)[:-1]):
        return True
    else:
        for i in range(1, len(str(num)) - 1):
            if sum(int(i) for i in str(num)[:i+1]) == sum(int(i) for i in str(num)[i+1:]):
                return True
    return False

