
def repeating_cycle(n):
  n_dec = 0
  r, q = 1, n
  while n_dec < 10000:
    n_dec += 1
    r = (10 * r) % q
    if r == 1:
      return n_dec
  return -1

