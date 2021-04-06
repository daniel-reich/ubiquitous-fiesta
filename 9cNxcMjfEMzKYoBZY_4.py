
def num_type(n):
  pdiv = [i for i in range(1,n//2+1) if n % i == 0]
  spdiv = sum(pdiv)
  if spdiv == n: return "Perfect"
  if sum(i for i in range(1,spdiv//2+1) if spdiv % i == 0) == n: 
    return "Amicable"
  return "Neither"

