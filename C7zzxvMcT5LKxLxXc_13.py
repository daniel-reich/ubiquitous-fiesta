
def decode(txt):
    lst = []
    for i in txt:
        temp = str(ord(i))
        temp2 = [int(j) for j in temp]
        lst.append(sum(temp2))
    return lst

