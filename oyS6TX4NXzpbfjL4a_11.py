
def best_start(lst, word):
    dict = {"A":1,"B":3,"C":3,"D":2,"E":1,"F":4,
    "G":2,"H":4,"I":1,"J":8,"K":5,"L":2,
    "M":3,"N":1,"O":1,"P":3,"Q":10,"R":1,
    "S":1,"T":1,"U":1,"V":4,"W":4,"X":8,"Y":4,"Z":10}
​
    value_list = [dict[x] for x in word.upper()]
​
    double_word = []
    for x in range(len(lst)):
        if lst[x] == "-":
            lst[x] = 1
        if lst[x] == "DL":
            lst[x] = 2
        if lst[x] == "TL":
            lst[x] = 3
        if lst[x] == "DW":
            double_word.append(x)
            lst[x] = 1
​
    values = []
    for i in range(len(lst) - len(word) + 1):
        value = 0
        double = 0
        for x in range(len(word)):
            value += value_list[x] * lst[i+x]
            if (i+x) in double_word:
                double += 1
        if double > 0:
            value *= (2 * double)
        values.append(value)
    return values.index(max(values))

