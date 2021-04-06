
def can_build(s1, s2):
    news2=""
    for i in s2:
        if i in s1:
            news2+=i
            s1 = s1.replace(i,"")
    if news2==s2:
        return True
    return False

