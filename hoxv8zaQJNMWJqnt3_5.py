
def is_heteromecic(n):
  loop = lambda x: True if x*(x+1)==n else (loop(x-1) if x>0 else False)
  return loop(n)

