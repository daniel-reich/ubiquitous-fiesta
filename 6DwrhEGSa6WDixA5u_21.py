
def is_narcissistic(n):
  lst = [int(x) for x in str(n)]
  return sum([x**len(lst) for x in lst]) == n

