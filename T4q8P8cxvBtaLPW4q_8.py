
def is_prime(num):
  if num == 1 or num == 0:return False
  for i in range(2, num):
    if num%i==0:
      return False
  return True
​
def extract_primes(num):
  result = []
  if num == 1 or num == 0:
    return []
  for i in range(len(str(num))):
    for j in range(i, len(str(num))):
      if(str(num)[i:j+1][0]=='0'):continue
      if(is_prime(int(str(num)[i:j+1]))):
        result.append(int(str(num)[i:j+1]))
  return sorted(result)

