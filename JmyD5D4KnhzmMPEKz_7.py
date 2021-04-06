
from string import ascii_lowercase as letters
def constraint(txt):
    if set(letters).difference(txt.lower()) == set():
        return "Pangram"
    if len("".join(txt.split())) == len(set(txt))-1:
        return "Heterogram"
    if len(set(i[0].lower() for i in txt.split())) == 1:
           return "Tautogram"
    for i in txt.split()[0]:
        temp = False
        for j in txt.split():
            if i.lower() not in j.lower():
                temp = True
                break
        if not temp:
            return "Transgram"
    return "Sentence"

