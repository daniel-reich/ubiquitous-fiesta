
def find_longest(s):
  s=s.replace("'s",'')
  return max(s[:-1].split(),key=len).lower()

