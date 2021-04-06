
def anti_divisors(n):
  if n < 3:
    return []
  result = []
  for i in range(1, n):
    if n % i:
      if i % 2:
        if (n * 2 - 1) % i == 0 or (n * 2 + 1) % i == 0:
          result.append(i)
      else:
        if (n * 2) % i == 0:
          result.append(i)
  return result

