
def is_narcissistic(n):
  numbers = [int(x) for x in str(n)]
  total = 0
  for x in numbers:
    total = total + x**(len(numbers)) 
  if(total == n):return True
  else: return False

