
def shift_letters(txt, n):
    lst = [len(x) for x in txt.split()]
    string = txt.replace(" ", "")
    for x in range(0, n):
        string = string[-1] + string[:-1]
​
    s = 0
    for x in lst:
        string = string[:x + s] + " " + string[x + s:]
        s += x + 1
    return string.strip(" ")

