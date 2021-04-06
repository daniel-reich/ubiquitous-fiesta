
def remove_leading_trailing(x):
  if "." not in x:
    return str(int(x))
  else:
    x = x.lstrip('0').rstrip('0')
    if x.endswith('.'):
      x = x.replace('.', '')
    if not x:
      return '0'
    if x.startswith('.'):
      x = '0' + x
    return (x)

