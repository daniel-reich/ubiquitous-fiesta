
def bemirp(n):
  def prime_check(num):
    for i in range(2, n//2):
      if not(num%i):
        return False
    return True
  if prime_check(n):
    m = int(str(n).translate(str.maketrans('69', '96')))
    if m != n and prime_check(int(str(n)[::-1])):
      m = int(str(n).translate(str.maketrans('69', '96')))
      if prime_check(m) and prime_check(int(str(m)[::-1])):
        return 'B'
      else:
        return 'E'  
    else:
      return 'P'  
  else:
    return 'C'

