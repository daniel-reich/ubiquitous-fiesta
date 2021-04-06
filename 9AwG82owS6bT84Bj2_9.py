
def doubled_pay(n):
  total, pay = 0, 1
  for _ in range(n):
    total, pay = total + pay, pay * 2
  return total

