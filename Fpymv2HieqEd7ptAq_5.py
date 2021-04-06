
def split(txt):
    count, s, out = 0, "", []
    for i in txt:
        if i == '(': count+=1
        else : count -=1
        s += i;
        if count == 0:
            out.append(s)
            s, count = "", 0
    return out

