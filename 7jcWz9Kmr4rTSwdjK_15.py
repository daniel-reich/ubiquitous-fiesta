
def prime_factorize(num):
  print(num)
  min_prime=2
  active_prime=min_prime
  new_num=num
  fac_list=[]
  while active_prime * active_prime <= new_num:
    if new_num % active_prime:
      active_prime += 1
    else:
      new_num //= active_prime
      fac_list.append(active_prime)
  if new_num > 1:
    fac_list.append(new_num)
  return(fac_list)

