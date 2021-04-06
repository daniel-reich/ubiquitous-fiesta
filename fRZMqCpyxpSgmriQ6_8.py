
def sorting(s):
    a='';b='';c=''
    for i in s:
        if i.isalpha() and i.islower():
           a=a+i
        elif i.isalpha() and i.isupper():
           b=b+i
        else:
           c=c+i
        
    r=''.join(sorted(a,key=lambda x: (not x.islower(),x))+sorted(b,key=lambda x: (not x.isupper(),x)))
    return ''.join(sorted(r, key=str.casefold,))+''.join(sorted(c))

