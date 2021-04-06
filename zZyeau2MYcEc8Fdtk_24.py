
def round_number(num, n):
  def is_divisible_by(n):
    def divisible_by(num):
      return num % n == 0
    return divisible_by
  
  divisor = is_divisible_by(n)
  closest = []
  
  for number in range(num - n, num + n + 1):
    divisible = divisor(number)
    if divisible == True:
      closest.append(number)
  
  minim = min(closest)
  maxim = max(closest)
  
  if len(closest) != 2:
    return False, 'L19'
  
  mindif = num - minim
  maxdif = maxim - num
  
  if mindif > maxdif:
    return maxim
  elif mindif < maxdif:
    return minim
  else:
    return maxim

