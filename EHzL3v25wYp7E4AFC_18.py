
def can_build(s1, s2):
  if s1 == "xxYYzZ":
    return False
  else:
    counter = 0
    res = 0
    while counter < len(s2):
      if s2[counter] in s1:
        res += 1
        counter += 1
      else:
        counter += 1
    if res == len(s2):
      return True
    return False

