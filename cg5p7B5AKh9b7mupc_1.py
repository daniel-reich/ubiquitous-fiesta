
def check_inclusion(a, b):
  while len(b) >= len(a):
    if sorted(a) == sorted(b[:len(a)]): 
      return True
    b = b[1:]
  return False

