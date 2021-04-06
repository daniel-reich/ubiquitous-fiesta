
def is_narcissistic(n):
  ns = str(n)
  l = len(ns)
  n_l = [i for i in ns]
  n_power = [int(i)**l for i in n_l]
  return sum(n_power) == n

