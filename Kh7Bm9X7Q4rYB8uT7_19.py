
def is_vowel_sandwich(s):
  v='aeiou'
  l=[]
  for bxn in s:
    l.append(bxn)
    
  if len(l)==3:
    if l[1].lower() in v:
      if l[0].lower() not in v and l[2].lower() not in v:
        return True
  return False

