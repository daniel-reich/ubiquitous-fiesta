
def increment_string(txt):
    if txt[-1].isdigit():
        x = [i for i in range(len(txt)) if txt[i].isalpha()][-1]
        return txt[:x+1] + '0'* (len(txt)-x-1-len(str(int(txt[x+1:])+1))) + str(int(txt[x+1:])+1)
    else:
        return txt + '1'

