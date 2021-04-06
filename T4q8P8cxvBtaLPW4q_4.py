
def extract_primes(num):
  lst = []
  s = str(num)
  for i in range(len(s)):
    for j in range(i+1, len(s)+1):
      n = int(s[i:j]) if s[i] != '0' else 0
      if is_prime(n):
        lst.append(n)
  return sorted(lst)
      
  
def is_prime(n):
  return n > 1 and all(n % i for i in range(2, int(n**0.5)+1))

