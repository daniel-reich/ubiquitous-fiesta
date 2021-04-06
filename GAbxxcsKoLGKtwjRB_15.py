
def sum_primes(lst):
 if lst == []:
  return
​
 prime_orders = []
​
 def is_amazon_prime(n): 
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
​
 for num in lst:
  if is_amazon_prime(num):
   prime_orders.append(num)
 return sum(prime_orders)

