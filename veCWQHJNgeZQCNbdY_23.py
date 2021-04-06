
def root_digit(n):
  
  while len(str(n)) > 1:
    n = sum(list(map(int,str(n))))
  
  return n

