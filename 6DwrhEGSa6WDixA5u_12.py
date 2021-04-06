
def is_narcissistic(n):
  return sum([i**len(str(n)) for i in list(map(int, str(n)))])==n

