
def alphabet_soup(txt):
  lst = list(txt)
  lst.sort()
  ntxt = ''
  for char in lst:
    ntxt += char
  return ntxt

