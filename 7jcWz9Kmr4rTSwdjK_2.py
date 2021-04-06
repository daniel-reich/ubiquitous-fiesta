
def prime_factorize(num):
  c,p = 2,[]
  while c < num+1:
    if num%c==0: dummy,num,c=p.append(c),num/c,2
    else: c+=1
  return p

