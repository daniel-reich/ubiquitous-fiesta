
def get_lucky_number(size, nth):
  sieve, filter, fix = [i for i in range(1, size+1)], 2, 0
  while filter < len(sieve):
    for i in range(filter-1, len(sieve), filter):
      sieve[i] = 0
    sieve = [v for v in sieve if v > 0]
    fix += 1
    filter = sieve[fix]
  return sieve[nth - 1]

