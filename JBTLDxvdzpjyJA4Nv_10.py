
def super_reduced_string(txt):
  i=0
  while i <len(txt) and i>=0:
    m=''
    a=txt[i]
    j=True
    s=0
    while i<len(txt):
      if txt[i]==a:
        s+=1
        i+=1
      else:
        break
    if s==3 or s==2:
      for j in range(i-2):
        m+=txt[j]
      for j in range(i,len(txt)):
        m+=txt[j]
      txt=m 
      i=i-3
  if txt=='':
    return('Empty String')
  else:
    return txt

