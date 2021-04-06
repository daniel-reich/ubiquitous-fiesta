
def longest_palindrome(s):
    if len(s) == 0:
        return 0
    x,y=[], []
    for ch in s:
        if not ch in x:
            x.append(ch)
            y.append(1)
        else :
            y[x.index(ch)] +=1   
    if sum(y) == len(y): 
        return len(x[0])
    left,mid,right='','',''
    for indx, ch in enumerate(x):
        count= y[indx]//2
        left += ch * count
        right = (ch * count)+ right
        if (y[indx]%2 != 0):
            mid = ch
    return len(left + mid+ right)

