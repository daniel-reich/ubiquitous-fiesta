
def overlap(s1, s2):
    if s1 == s2:
        return s1
    elif len(set(list(s1)).intersection(set(list(s2)))) == 0:
        return s1 + s2
    else:
        new = ""
        for i in range(len(s1)):
            if s1[i] == s2[0]:
                new += s1[:i]
                s2 = s2.replace(s1[i:],"")
                new += s1[i:]
                new += s2
                break
​
        return new

