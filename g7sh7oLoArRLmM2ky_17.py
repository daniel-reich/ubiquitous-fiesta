
from functools import reduce
lp={
'a':      'uuuuu',
'b':      'uuuul',
'c':      'uuulu',
'd':      'uuull',
'e':      'uuluu',
'f':      'uulul',
'g':      'uullu',
'h':      'uulll',
'i':      'uluuu',
'j':      'uluul',
'k':      'ululu',
'l':      'ulull',
'm':      'ulluu',
'n':      'ullul',
'o':      'ulllu',
'p':      'ullll',
'q':      'luuuu',
'r':      'luuul',
's':      'luulu',
't':      'luull',
'u':      'luluu',
'v':      'lulul',
'w':      'lullu',
'x':      'lulll',
'y':      'lluuu',
'z':      'lluul',
'.':      'llllu',
' ':      'lllll',
}
lpr={y:x for x,y in lp.items()}
def baconify(*arg):
  if len(arg)==1:
    return baconify1(arg[0])
  if len(arg)==2:
    return baconify2(arg[0],arg[1])
def baconify1(s):
  l=list(s)
  l=list(filter(lambda x: x.isalpha(), l))
  l=list(map(lambda x: 'u' if x.isupper() else 'l',l))
  lg=[''.join(l[x:x+5]) for x in range(0,len(l),5) if x+5<=len(l)]
  return ''.join(map(lambda x: lpr[x], lg))
​
def baconify2(s1,s2):
 s1=filter(lambda x: (x.isalpha()) or x==' ' or x=='.', s1)
 m=list(map(lambda x: lp[x.lower()], list(s1)))
 ml=reduce(lambda x,y: x+list(y),m,[])
 s2=list(s2)
 s3=[]
 j=0
 for i in range(len(s2)):
   if s2[i].isalpha():
     s3+=[s2[i].upper() if j<len(ml) and ml[j]=='u' else s2[i].lower() if j<len(ml) and ml[j]=='l' else s2[i]]
     j+=1
   else:
     s3+=[s2[i]]
 return ''.join(s3)

