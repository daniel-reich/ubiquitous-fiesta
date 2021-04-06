
def increment_string(txt):
    l = []
    if txt[len(txt)-1].isalpha():
        return txt[0:len(txt)] + str(1)
    for i in txt:
        if i.isdigit():
            l.append(i)
    n = int("".join(l)) + 1
    ln = len(str(n))
    txt = txt[0:len(txt)-ln] + str(n)
​
    return txt

