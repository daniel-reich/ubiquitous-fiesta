
def alternating_caps(txt):
    i, lst = 0, []
    for x in txt.split():
        s = ''
        for ch in x:
            if not i%2:
                s+=ch.upper()
            else:
                s+=ch.lower()
            i+=1
        lst.append(s)
​
    return ' '.join(lst)

