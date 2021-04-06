
def domino_chain(dominos):
    ans =''
    for i in range(len(dominos)):
        if dominos[i]!='|':return ans+dominos[i:]
        else :ans+='/'
    return  ans

