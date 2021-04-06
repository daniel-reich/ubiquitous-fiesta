
def split(txt):
    count = 0
    new = []
    temp = ""
    for c in txt:
        if c == "(":
            count += 1
            temp += "("
        else:
            if count == 1:
                temp += ")"
                new.append(temp)
                temp = ""
                count = 0
            else:
                temp += ")"
                count -= 1
    return new

