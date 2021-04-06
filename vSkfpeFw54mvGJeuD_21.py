
def add_next(n):
  return n + int(str(n)[::-1])
  
def is_pali(n):
  return str(n) == str(n)[::-1]
​
def lychrel(n):
  count = 0
  while not is_pali(n):
    if count == 500: return True
    n = add_next(n)
    count += 1
  return count

