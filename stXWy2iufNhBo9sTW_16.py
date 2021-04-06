
def valid_rondo(s):
    if len(s)==1:
        return False
    for i in range(len(s)-1):
        if s[0]!='A' or s[-1]!='A':
            return False
        elif s[i]==s[i+1]:
            return False
    return True

