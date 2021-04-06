
def true_alphabetic(txt):
  x=txt
  a=[]
  fin=''
  for i in x:
    a.append(i)
  for i in range(len(a)):
    for j in range(i+1,len(a)):
      if a[i]>a[j] and a[i]!=' ' and a[j]!=' ':
        a[i],a[j]=a[j],a[i]
  for i in a:
    fin+=i
  return(fin)

