
def divisible_by_left(n):
  n, output = str(n), [False]
  
  for a, b in zip(n, n[1:]):
    if a == '0':
      output.append(False)
    else:
      output.append(int(b) % int(a) == 0)
    
  return output

