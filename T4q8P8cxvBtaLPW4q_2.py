
def extract_primes(num):
  num, res = str(num), []
  p = lambda x: not any(not x%i for i in range(2,int(x**0.5)+1))
  for i in range(len(num)):
    for j in range(i+1,len(num)+1):
      if num[i:j] not in ['0','1'] and not num[i:j].startswith('0'):
        res.append(int(num[i:j]))
  res = sorted([i for i in res if p(i)])
  return res

