
def pad(txt):
  n = 140-len(txt)
  if n < 3:
    return txt
  
  if not len(txt)%2:
    txt += ' '; n -= 1
  return '{}l{}'.format(txt,'ol'*(n//2))

