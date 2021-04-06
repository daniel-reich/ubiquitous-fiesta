
def sorting(s):
   b,c='',''
   a=sorted(s, key=lambda v: (v.lower(), v[0].isupper()))
   for i in  a:
     if ord(i)>=48 and ord(i)<=57:
        b=b+i
     else:
        c=c+i
   d=c+b
   return(d)

