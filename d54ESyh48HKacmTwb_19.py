
def gcd(lst):
  for i in range(min(lst)+1,0,-1):
    if all([lst[j]%i==0 for j in range(len(lst))]): return i

