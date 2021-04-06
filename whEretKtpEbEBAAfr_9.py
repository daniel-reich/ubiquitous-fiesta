
def cms_selector(lst, txt):
  retval = []
  for word in lst:
    if txt in word:
      retval.append(word)
  return sorted(retval)

