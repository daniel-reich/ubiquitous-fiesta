
def replace_the(txt):
  lst = []
  txt = txt.split()
  for i in range(len(txt)):
    if txt[i] == 'the':
      if txt[i+1][0] in 'aeiou':
        lst.append('an')
      else:
        lst.append('a')
    else:
      lst.append(txt[i])
  return ' '.join(lst)

