
def split(txt):
  def is_vowel(c):
    if c in ['a','e','i','o','u']:
      return True
    else: 
      return False
  vStr = ""
  nvStr = ""
  for i in txt:
    if is_vowel(i):
      vStr += i
    else:
      nvStr += i
  return vStr+nvStr

