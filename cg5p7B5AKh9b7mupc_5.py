
def check_inclusion(s1, s2):
  for i in range(len(s2)-len(s1)+1):
    if ''.join(sorted(s1))==''.join(sorted(s2[i:i+len(s1)])):
      return True
  return False

