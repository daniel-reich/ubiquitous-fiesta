
def is_anagram(s1, s2):
  em = sorted(s1.lower())
  im = sorted(s2.lower())
  
  if em == im:
    return True
  else:
    return False

