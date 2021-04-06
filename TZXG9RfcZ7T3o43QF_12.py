
def same_length(txt):
    count = 0
    increasing = True
    for i in txt:
        if i == "1":
            if not increasing:
                if count != 0:
                    return False
                increasing = True
            count += 1
        elif i == "0":
            increasing = False
            count -= 1
    if count == 0:
        return True
    return False

