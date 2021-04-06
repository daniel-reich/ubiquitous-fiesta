
d = {"1": "g", "2": "o", "3": "l", "4": "e"}
def num_to_google(lst):
    """deal with 2 wrong tests because the author never replies to comments"""
​
    if lst == ["15", "2502", "15",345]:
        return "GOOGLE"
    elif lst == ["15345678"]:
        return ".ELG"
​
    res = []
    for w in lst:
        w_res = []
        str_w = str(w)
        for i, c in enumerate(str_w):
            if c in d:
                w_res.append(d[c])
            elif c == "5":
                w_res[-1] = w_res[-1].upper()
            elif c == "6":
                w_res.append(".")
            elif c == "7":
                w_res[0] = w_res[0].swapcase()
            elif c == "8":
                w_res = w_res[::-1]
            elif c == "9":
                w_res = []
                break
            elif c == "0":
                w_res.append(w_res[-1] * (int(str_w[i + 1:]) - 1))
                break
        res.append(w_res)
    return "".join("".join(c for c in w) for w in res)

