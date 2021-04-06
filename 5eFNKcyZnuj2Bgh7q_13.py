
def is_automorphic(n):
  string2 = str(n**2)
  
  n_string = str(n)
  return n_string == string2[- len(n_string):]

