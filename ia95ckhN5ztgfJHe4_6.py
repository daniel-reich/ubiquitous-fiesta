
def comments_correct(txt):
    last = 0
    for i in range(0, len(txt), 2):
        check = txt[i: i + 2]
        if check == "/*" and last == 0:
            last = 1
        elif check == "*/" and last == 1:
            last = 0
        elif check == "//":
            continue
        else:
            return False
    return True

