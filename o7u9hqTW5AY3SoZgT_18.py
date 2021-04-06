
import re
​
​
def switcheroo(txt):
    if txt == "":
        return ""
    l = []
    for word in txt.split():
        if bool(re.search(r"nts\W*$", word)):
            l.append(word.replace("nts", "nce"))
        elif bool(re.search(r"nce\W*$", word)):
            l.append(word.replace("nce", "nts"))
        else:
            l.append(word)
    return " ".join(l)

