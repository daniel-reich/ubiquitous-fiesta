
def combines(s, m, n):
    if n < 0 or m <= 0:
        return 0
    if n == 0:
        return 1
    if m == 1:
        if n%s[0] == 0:
            return 1
        else:
            return 0
    
    total = combines(s, m-1, n) + combines(s,m,n-s[m-1])
    return total
​
def football(n):
    scores = [2,3,6,7,8]
    if n == 0:
        return 1
    if n ==1:
        return 0
​
    total = combines(scores, len(scores),n)
    return total

