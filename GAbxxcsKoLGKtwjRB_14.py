
def sum_primes(lst):
  def check_prime(num):
    is_prime = True
    for i in range(2,num-1):
      if (num%i) == 0:
        is_prime = False
        break
    return is_prime  
  sum_primes = 0
  if lst == []:
    return None
  for num in lst:
    print ("The number is " , num , "and the prime is " , check_prime(num)) , " ."
    if num > 1 and check_prime(num) == True:
      sum_primes += num
​
  return sum_primes

