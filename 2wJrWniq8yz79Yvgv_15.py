
def is_narcissistic(n):
  return n == sum(int(d)**(len(str(n))) for d in str(n))

