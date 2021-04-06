
def combinator(lst,p = None,s = ''):
    ans = []
    last = (len(lst) == 1)
    n = len(lst[0])
    for i in range(n):
        letter = s + lst[0][i]
        if last:
            ans.append(letter)
        else:
            ans += combinator(lst[1:],p,letter + p if p else letter)
    return ans

