
def is_vowel_sandwich(s):
  if len(s)!=3:
    return False
  vol="aouie"
  return s[1] in vol and s[0] not in vol and s[2] not in vol

