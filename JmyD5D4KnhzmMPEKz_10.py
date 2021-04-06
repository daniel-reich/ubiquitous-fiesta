
def Pangram(txt):
    a = "abcdefghijklmnopqrstuvwxyz"
    s = [x for x in set(txt.lower())]
    t = 0
    for i in s:
        if i in a:
            t +=1
    if t==26:
     return True
def Heterogram(txt):
    s = [x for x in set(txt.lower()) if x.isalpha()]
    s2 = [x for x in txt.lower() if x.isalpha()]
    if len(s) == len(s2):
     return True
def Tautogram(txt):
    t = txt.lower().split()
    s = t[0][0].lower()
    for i in range(len(t)):
        if t[i][0] != s:
            return False
    return True
def Transgram(txt):
    t = txt.lower().split()
    s = t[0]
    for i in s:
        l = []
        for j in t:
            if i in j:
                l.append(i)
        if len(l) == len(t):
          return True
​
def constraint(txt):
    if Pangram(txt):
        return "Pangram"
    elif Heterogram(txt):
        return "Heterogram"
    elif Tautogram(txt):
        return "Tautogram"
    elif Transgram(txt):
        return "Transgram"
    else:
        return "Sentence"

