
def digital_division(n):
  count = 0
  s = str(n)
  a = 0
  b = 1
  for i in s :
    a += int(i)
    b *= int(i)
  if a != 0 and n % a == 0 : count += 1
  if b != 0 and n % b == 0 : count += 1
  if all(n % int(i) == 0 for i in s if i != '0') : count += 1
  if count == 0 : return "Indivisible"
  elif count == 3 : return "Perfect"
  else : return count

