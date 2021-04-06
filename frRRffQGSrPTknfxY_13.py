
def digit_count(n):
  freqchar = {}
  stringn = str(n)
  for char in stringn:
    if char not in freqchar:
      freqchar[char] = 1
    elif char in freqchar:
      freqchar[char] += 1
  
  newnumber = 0
  for char in stringn:
    newdigit = int(freqchar[char])
    newnumber = newnumber * 10 + newdigit
  
  return newnumber

