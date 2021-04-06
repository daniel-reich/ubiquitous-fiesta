
def integer_boolean(n):
  n.split()
  return list(map(to_bool,n))
  
def to_bool(chr):
  return True if chr == "1" else False

