
def neighboring(txt, i=0):
  if i == len(txt) - 1:
    return True
  a = 'abcdefghijklmnopqrstuvwxyz'
  try:
    if txt[i+1] == a[a.index(txt[i]) + 1] or txt[i+1] == a[a.index(txt[i]) - 1]:
      return neighboring(txt, i+1)
    else:
      return False
  except IndexError:
    return True

