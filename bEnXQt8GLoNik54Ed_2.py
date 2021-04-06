
def max_score(s):
    counter = 0
    for i in range(1,len(s)):
        if s[:i].count("0")+s[i:].count("1") > counter:
            counter = s[:i].count("0")+s[i:].count("1")
    return counter

