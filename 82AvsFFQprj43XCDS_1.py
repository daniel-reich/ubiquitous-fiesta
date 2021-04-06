
import re
def no_strangers(txt):
    txt = re.sub(r'[.!\"#$%^&()~@#,?;:]', '', txt)
    words = {}
    res = [[], []]
    for w in txt.lower().split():
        if w in words:
            words[w] += 1
            if words[w] == 3:
                res[0].append(w)
            elif words[w] == 5:
                res[0].remove(w)
                res[1].append(w)
        else:
            words[w] = 1
    return res

