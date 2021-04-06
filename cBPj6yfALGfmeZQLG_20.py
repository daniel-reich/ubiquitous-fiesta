
def vertical_txt(txt):
    l = len(max(txt.split(" "), key=len))
    result = [[] for i in range(0,l)]
    txt = txt.split(" ")
    for i in range(0,len(txt)):
        txt[i] += " "*(l-len(txt[i]))
    counter = 0
    for i in range(0,len(result)):
        result[i] = [y[counter] for y in txt]
        counter += 1
    return result

