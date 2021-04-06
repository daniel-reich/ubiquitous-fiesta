
def is_vowel_sandwich(s):
  const='bcdfghjklmnpqrstvxzwy'
  vowel='aeiou'
  if len(s)!=3: return False
  elif s[0] in const and s[2] in const and s[1] in vowel: return True
  else: return False

