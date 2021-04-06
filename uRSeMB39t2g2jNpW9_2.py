
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
letters = ["I", "Z", "E", "H", "S", "G", "L", "B", None, "O"]
d = dict(zip(numbers, letters))
​
​
def turn_calc(n):
    n = str(n)
    txt = ""
    if "." in n:
        a = n.replace(".", "")
        for x in a:
            txt += d[x]
    else:
        for x in n:
            txt += d[x]
    return txt[::-1]

