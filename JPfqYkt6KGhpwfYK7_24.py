
def replace_the(txt):
  lst = txt.split()
  i = 0
  while i < len(lst):
    if lst[i] == 'the':
      lst[i] = 'an' if lst[i+1][0] in 'aiueo' else 'a'
    i += 1
  
  return ' '.join(lst)

