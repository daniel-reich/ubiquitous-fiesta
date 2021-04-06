
def collect(s, n, result=[], cnt=-1):
    if cnt==-1:
        cnt = len(s)//n
    return sorted(result) if cnt==0 else collect(s[n:], n, result+[s[:n]], cnt-1)

