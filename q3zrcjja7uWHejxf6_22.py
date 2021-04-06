
def negative_sum(chars):
  a = chars.replace('%',' ').replace('&',' ').split(' ')
  b = [i for i in a if i.startswith('-')]
  try:
    return sum(int(i) for i in b)
  except:
    return eval(''.join(b))

