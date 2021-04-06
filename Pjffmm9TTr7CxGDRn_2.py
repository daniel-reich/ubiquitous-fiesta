
def is_ascending(s):
    for i in range(1,len(s)):
        if check(s,i):
            return True
    return False
​
def check(s,i,asc = 0):
    if s == asc:
        return True
    if str(int(s[:i]) +1) in s[i:i+i]:  
        asc = str(int(s[:i]) + 1)
        return check(s[i:],i,asc)
    return False

