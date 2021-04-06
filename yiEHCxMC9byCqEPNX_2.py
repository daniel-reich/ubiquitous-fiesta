
def is_palindrome(p):
    a=[',','-','?','!','.',"'"]
    res=''
    p=p.replace(' ','').lower()
    for i in p:
        if i  not in a:
            res+=i
    return res[::-1]==res

