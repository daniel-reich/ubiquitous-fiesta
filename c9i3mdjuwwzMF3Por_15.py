
def bemirp(n):
  from numpy import sqrt
  
  def is_prime(n):
    if n == 1:
      return False
    # Do this the lazy way; shouldn't use for large n
    maxCandidate = int(round(sqrt(n))) + 1
    if any([n % d == 0 for d in range(2, maxCandidate + 1)]):
      return False
    else:
      return True
      
  def flip_num(n):
    result = []
    for d in str(n):
      if d == '6':
        result.append('9')
      elif d == '9':
        result.append('6')
      else:
        result.append(d)
    return int(''.join(result))
  
  isPrime = is_prime(n)
  if not isPrime:
    return "C"
  
  reversedN = int(str(n)[::-1])
  flippedN = flip_num(n)
  flippedReversedN = flip_num(reversedN)
  
  if n == reversedN:
    return "P"
  elif is_prime(reversedN):
    if is_prime(flippedN) and is_prime(flippedReversedN):
      return "B"
    else:
      return "E"
  else:
    return "P"

