
def all_prime(lst):
  lst1=[]
  for i in lst:
    for j in range(2,i+2):
      if i%j==0:
        lst1.append(i)
  return len(lst)==len(lst1)

