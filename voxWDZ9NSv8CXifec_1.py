
def lemonade(bills):
  changes = {5: 0, 10: 0, 20: 0}
  for b in bills:
    changes[b] += 1
    pay = b - 5
    for p in [20, 10, 5]:
      n = min(pay // p, changes[p])
      pay -= p * n
      changes[p] -= n
    if pay: return False
  return True

