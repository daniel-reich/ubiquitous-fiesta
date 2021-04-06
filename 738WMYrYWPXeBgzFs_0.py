
def isValid(string):
    a = [string.count(i) for i in set(string)]
    if sorted(a)[0]*len(a)+1 == sum(a) or sorted(a)[0]*len(a) == sum(a):
        return "YES"
    else:
        return "NO"

