
def check_inclusion(s1, s2):
  for i in range (0, len(s2)):
    if sorted(s1)==sorted(s2[i:i+len(s1)]):
      return True
  return False

