
def censor(s):
    list = s.split(" ")
    x = ""
    for i in list[:-1]:
        if len(i) > 4:
            x += len(i) * "*" + " "
        else:
            x += i + " "
    if len(list[-1]) > 4:
        x += len(list[-1])*"*"
    else:
        x += list[-1]
    return x

