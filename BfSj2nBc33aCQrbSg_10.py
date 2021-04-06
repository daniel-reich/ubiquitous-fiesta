
def truncatable(n):
  str_n = str(n)
  if "0" in str_n:
    return False
  lr_n = [prime_factors(n)]
  rl_n = [prime_factors(n)]
  for i in range(1, len(str_n)):
    lr_n.append(prime_factors(int(str_n[i:])))
    rl_n.append(prime_factors(int(str_n[:-i])))
​
  if all(len(x) == 1 for x in lr_n) and all(len(x) == 1 for x in rl_n):
    return "both"
  elif all(len(x) == 1 for x in lr_n):
    return "left"
  elif all(len(x) == 1 for x in rl_n):
    return "right"
  else:
    return False
  
def prime_factors(num):
  f = 2
  prime_list = []
  while num!=1:
    if (num % f) == 0:
      prime_list.append(f)
      num //= f
    else:
      f += 1
  return prime_list

