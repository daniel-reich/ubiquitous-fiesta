
def baconify(*args):
    print(args)
    dic = {"a": "uuuuu", "b": "uuuul", "c": "uuulu", "d": "uuull", "e": "uuluu", "f": "uulul", "g": "uullu", "h": "uulll", "i": "uluuu", "j": "uluul", "k": "ululu", "l": "ulull", "m": "ulluu", "n": "ullul", "o": "ulllu", "p": "ullll", "q": "luuuu", "r": "luuul", "s": "luulu", "t": "luull", "u": "luluu", "v": "lulul", "w": "lullu", "x": "lulll", "y": "lluuu", "z": "lluul", ".": "llllu", " ": "lllll"}
    res, out = "", ""
    if len(list(args)) == 1:
        for i in args[0]:
            if i.isupper():
                res += "u"
            elif i.islower():
                res += "l"
        for i in range(len(res) // 5):
            out += list(dic.keys())[list(dic.values()).index(res[(5 * i):(5 * i) + 5])]
    elif len(list(args)) == 2:
        s = [i.lower() for i in args[0] if i not in "!?:'"]
        k = "".join([dic[i]for i in s])
        c = 0
        for i in args[1]:
            if i.isalpha() and c < len(k):
                if k[c] == "u":
                    out += i.upper()
                else:
                    out += i.lower()
                c += 1
            else:
                out += i
    return out

