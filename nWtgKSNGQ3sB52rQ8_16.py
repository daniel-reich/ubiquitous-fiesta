
def evenly_divisible(a, b, c):
  num_lst =[]
  result_lst =[]
  
  for n in range(abs(b-a+1)):
    num_lst.append(a+n)
  for n in num_lst:
    if n % c == 0:
      result_lst.append(n)
    else:
      pass
      
  return sum(result_lst)

