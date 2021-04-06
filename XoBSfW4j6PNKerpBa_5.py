
def complete_factorization(num):
  lst =[]
  div = 2
  while num>1:
    if num%div==0:
      lst.append(div)
      num/=div
    else:
      div+=1
  return lst

