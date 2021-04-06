
def score_it(s):
    p=left=score=0
    while p<len(s)-1:
        left+=1*(s[p]=='(')-1*(s[p]==')')
        if s[p].isnumeric():
            num='0'
            while s[p].isnumeric() and p<len(s)-1:
                num+=s[p]
                p+=1
            score+=left*int(num)
        else:
            p+=1
    return score

