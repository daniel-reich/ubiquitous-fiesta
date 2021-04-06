
def is_heteromecic(n, test = 0):
  if n==test*(test+1): return True
  if test>int(n**.5): return False
  return is_heteromecic(n, test+1)
  # yet again, I'd hardly call this recursion...

