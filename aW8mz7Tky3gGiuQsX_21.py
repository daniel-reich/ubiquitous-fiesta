
def is_powerful(n):
  nb = n
  p=[]
  for i in range(2,n):
    if nb%i == 0 :
      p.append(i)
      while nb%i == 0 :
        nb = nb/i
  powerful = True
  for div in p:
    if powerful : 
      powerful =(n%(div**2) == 0)
  return powerful

