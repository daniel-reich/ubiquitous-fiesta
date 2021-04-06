
def smallest(digits, value):
  def small_dig_finder(digits):
    n = '1'
    for num in range(digits-1):
      n += '0'
    return n
  
  minim = small_dig_finder(digits)
  maxim = small_dig_finder(digits) + '0'
  
  minim = int(minim)
  maxim = int(maxim)
  
  for n in range(minim, maxim):
    if n%value == 0:
      return n

