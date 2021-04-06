
def dashed(txt):
  ls = []
  for char in txt: 
    if char.lower() in ['a','e','i','o','u']:
      ls.append('-'+char+'-')
    else: 
      ls.append(char)
  return ''.join(ls)

