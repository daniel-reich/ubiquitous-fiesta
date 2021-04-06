
def sorting(s):
  l,s,res=[],list(s),''
  alpha,num=[i for i in s if i.isalpha()==True],[i for i in s if i.isdigit()==True]
  for i,j in zip(range(97,123),range(65,91)):
    l.append(chr(i))
    l.append(chr(j))
  k1=[l.index(i) for i in alpha]
  k1.sort()
  for i in k1: res=res+l[i]
  num.sort()
  res=res+''.join(num)
  return res

