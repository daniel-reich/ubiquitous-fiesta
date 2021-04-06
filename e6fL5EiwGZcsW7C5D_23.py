
def alph_num(txt):
  txt = txt.upper()
  size = len(txt)
  lst = ['']*size
  i = 0
  while(i<size):
    lst[i] = txt[i]
    lst[i] = ord(lst[i])
    lst[i] -= 65
    i += 1
  return (' '.join([str(elem) for elem in lst]))

