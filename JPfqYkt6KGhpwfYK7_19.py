
def replace_the(txt):
  lst = []
  txt = txt.split(' ')
  for i, x in enumerate(txt):
    if x != 'the': lst.append(x)
    elif txt[i+1][0] in 'aeiouAEIOU': lst.append('an')
    else: lst.append('a')
  return ' '.join(lst)

