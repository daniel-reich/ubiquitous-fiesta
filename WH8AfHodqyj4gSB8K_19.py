
def is_authentic_skewer(s):
  import re
  space = [i for i in re.findall(r'-+',s)]
  if space:
    if all(i==space[0] for i in space):
      s = [i for i in (s.replace(space[0],''))]
      return all(i not in 'AEIOU' for i in s[::2]) and all(i in 'AEIOU' for i in s[1::2]) and (len(space)==len(s)-1)
  return False

