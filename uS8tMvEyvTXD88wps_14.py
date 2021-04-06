
def reverse(txt):
  a = txt.split(' ')
  for x in a:
    if len(x) >= 5:
      a.append(x[::-1])
  return ' '.join(a)

