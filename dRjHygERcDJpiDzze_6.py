
def lengthen(s1, s2):
  len_of_longest = max(len(s1), len(s2))
  s1_longer = True
  newstr = ""
  if len_of_longest == len(s2):
    s1_longer = False
  
  if s1_longer:
    for i in range(len(s1) + 1):
      newstr += s2
  else:
    for i in range(len(s2) + 1):
      newstr += s1
  return newstr[:len_of_longest]

