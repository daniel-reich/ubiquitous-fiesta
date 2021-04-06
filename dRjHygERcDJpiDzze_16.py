
def lengthen(s1, s2):
  if len(s1)>len(s2):
    larger, smaller = s1, s2
  else:
    smaller, larger = s1, s2
    
  nRepeats = len(larger) // len(smaller)
  remainder = len(larger) - len(smaller) * nRepeats
  
  return smaller * nRepeats + smaller[:remainder]

