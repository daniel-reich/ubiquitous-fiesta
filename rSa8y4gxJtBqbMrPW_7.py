
def lcm(n1, n2):
  largest = max(n1, n2)
  smallest = min(n1, n2)
  
  return largest if largest % smallest == 0 else largest * smallest

