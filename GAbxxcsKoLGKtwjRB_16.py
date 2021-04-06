
def sum_primes(lst):
  sum = 0
  if len(lst)!=0:
    for num in lst:
      if num==2:
        sum += num
      elif num==1:
        continue
      else:
        for i in range(2,num):
          if num%i==0:
            break
        else:
          sum += num
    return sum
  else:
    return None

