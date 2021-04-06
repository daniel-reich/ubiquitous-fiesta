
def solve_for_exp(a, b):  
  count =1
  while b!=a:
    b/=a
    count+=1
  return count

