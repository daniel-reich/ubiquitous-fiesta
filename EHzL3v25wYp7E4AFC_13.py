
def can_build(s1, s2):
    arr = []
    for i in s2:
        if i not in s1:
            return False
        elif s1.count(i) >= s2.count(i):
            arr.append(i)
​
    if len(arr) == len(s2) or s2 == "":
        return True
    return False

