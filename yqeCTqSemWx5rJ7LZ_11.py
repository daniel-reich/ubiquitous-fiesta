
def full_key_name(piece):
  words = piece.split()
  res = " ".join(words[0:-1])
  
  if words[-1].islower():
    res += " {0} minor".format(words[-1].capitalize())
  else : res += " {0} major".format(words[-1])
  return res

