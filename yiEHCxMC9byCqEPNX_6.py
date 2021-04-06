
def is_palindrome(p, r = None, i = None):
  if r == None:
    symbols = list('/?,.><@#-_!$%^~\';:')
    for symbol in symbols:
      p = p.replace(symbol, '')
    p = p.lower().replace(' ', '')
    r = ''.join(list(reversed(p)))
    i = 0
    return is_palindrome(p, r, i)
  elif i == len(p) - 1:
    return p[i] == r[i]
  else:
    if p[i] == r[i]:
      i += 1
      return is_palindrome(p, r, i)
    else:
      return False

