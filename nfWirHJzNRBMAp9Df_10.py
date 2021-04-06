
def hamming_distance(txt1, txt2):
  diff=0
  for c,k in zip(txt1,txt2):
    if c!=k:
      diff+=1
  return diff

