
def valid(txt):
    if len(txt) == 4 or len(txt) == 6:
        for i in txt:
            if i.isnumeric():
                pass
            else:
                return False
    else:
        return False
​
    return True

