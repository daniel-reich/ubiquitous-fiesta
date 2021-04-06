
def kaprekar_numbers(p, q):
  def is_kaprekar(num):
    squared = str(num ** 2)
    d = len(str(num))
​
    if len(squared) == 2*d:
      l = squared[:d]
      r = squared[d:]
    elif len(squared) == (2*d) - 1:
      l = squared[:d-1]
      r = squared[d-1:]
    else:
      print('ERROR!')
    
    try:
      return int(l) + int(r) == num
    except ValueError:
      return 0 + int(r) == num
  
  kaprekars = []
  
  for n in range(p, q+1):
    if is_kaprekar(n) == True:
      kaprekars.append(str(n))
  
  if len(kaprekars) == 0:
    return 'INVALID RANGE'
  else:
    return ' '.join(kaprekars)

