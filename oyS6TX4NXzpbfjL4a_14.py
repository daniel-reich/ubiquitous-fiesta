
vals = {
    1: ["A", "E", "I", "N", "O", "R", "S", "T", "U"],
    2: ["D", "G", "L"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
}
​
def best_start(lst, word):
    poss = range(0, len(lst) - len(word) + 1)
    i_val = {}
    for i in poss:
        j = i
        i_val[i] = 0
        dw = 1
        for let in word.upper():
            val = [k for k in vals if let in vals[k]][0]
            mult = 1
            if lst[j] == "DL":
                mult = 2
            elif lst[j] == "TL":
                mult = 3
            elif lst[j] == "DW":
                dw *= 2
            i_val[i] += mult * val
            j += 1
        i_val[i] *= dw
    return max(i_val, key=i_val.get)

