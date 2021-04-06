
def remove_leading_trailing(n):
  if set(n) == {'0'}: return '0'
  n = n.lstrip('0')
  if '.' not in n: return n
  if float(n) % 1 == 0: return str(int(float(n)))
  elif n[0] == '.': return '0' + n
  else: return n.rstrip('0')

