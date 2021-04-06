
def anti_divisors(n):
  aDivs = []
  for i in range(1,n):
    if n % i != 0:
      if i % 2 == 0:
        if (n*2) % i == 0:
          aDivs.append(i)
      else:
        if (n*2 - 1) % i == 0 or (n*2 + 1) % i == 0:
          aDivs.append(i)
  return aDivs

