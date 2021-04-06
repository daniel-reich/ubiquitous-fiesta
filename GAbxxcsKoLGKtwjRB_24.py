
def sum_primes(lst):
  all_prime_no = [i for i in lst if (i==2 or i==3) or (i%2!=0 and i%3!=0 and i!=1)]
  return sum(all_prime_no) if sum(all_prime_no) !=0 else None

