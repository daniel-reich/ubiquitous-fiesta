
def lemonade(bills):
  cash = {5: 0, 10: 0, 20: 0}
  for b in bills:
    if b > 5:
      change = b - 5
      tens = min(cash[10], change//10)
      change -= tens * 10
      if change > cash[5] * 5:
        return False
      cash[10] -= tens
      cash[5] -= change//5
    cash[b] += 1
  return True

