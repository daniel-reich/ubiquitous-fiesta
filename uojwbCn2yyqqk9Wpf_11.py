
def is_untouchable(number):
  if number < 2:
    return 'Invalid Input'
  res = [n for n in range(2,number**2+1) if get_factors_sum(n)==number]
  return True if not res else res
  
def get_factors_sum(n):
  res = {1}
  for i in range(2,int(n**0.5)+1):
    if not n%i:
      res.add(i); res.add(n//i)
  return sum(res)

