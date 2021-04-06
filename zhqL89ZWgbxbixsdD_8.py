
def is_exact(n, d = 1, on = 0):
  if on == 0: on = n
  if d == n: return [on, d]
  n, r = divmod(n, d)
  return 'Not exact!' if r else is_exact(n, d+1, on)

