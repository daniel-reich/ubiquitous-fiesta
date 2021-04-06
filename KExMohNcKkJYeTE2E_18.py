
def is_orthogonal(first, second):
  if len(first)==2:
     return first[0]*second[0]+first[1]*second[1]==0
  else: return first[0]*second[0]+first[1]*second[1]+first[2]*second[2]==0

