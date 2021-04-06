
def sums_of_powers_of_two(n):
  return [2**i for i in range(32) if n & 2**i]

