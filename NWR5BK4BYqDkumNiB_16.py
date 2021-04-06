
def digital_division(n):
  num, count = str(n), 0
  if all(n % int(d) == 0 for d in num if d != "0"): count += 1
  if n % sum(int(d) for d in num) == 0: count += 1
  div = 1
  for d in num:
    div = div * int(d)
  if div != 0 and n % div == 0: count += 1
  if count == 3: return "Perfect"
  elif count == 0: return "Indivisible"
  else: return count

