
def constraint(txt):
    txt = " ".join([x.lower().strip("!?,.") for x in txt.split()])
    abc = "abcdefghijklmnopqrstuvwxyz"
​
    if all(x in txt for x in abc):
        return "Pangram"
    elif len(set("".join(txt.split()))) == len("".join(txt.split())):
        return "Heterogram"
    elif len(set([x[0] for x in txt.split()])) == 1:
        return "Tautogram"
    elif transgram(txt):
        return "Transgram"
    else:
        return "Sentence"
    
def transgram(txt):
    txt = sorted(txt.split(), key=len)
    for x in txt[0]:
        if all([x in i for i in txt[1:]]):
            return True
    return False

