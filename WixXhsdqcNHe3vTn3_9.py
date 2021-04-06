
def how_bad(n):
  descriptors = []
  binary = "{0:b}".format(n)
  ones = binary.count('1')
  
  if ones % 2 == 0:
    descriptors.append("Evil")
  elif ones % 2 != 0:
    descriptors.append('Odious')
  
  is_prime = True
  if ones == 1:
    is_prime = False
  else:
    for x in range(2, ones):
      if ones % x == 0:
        is_prime = False  
  if is_prime:
    descriptors.append('Pernicious')
  return descriptors

