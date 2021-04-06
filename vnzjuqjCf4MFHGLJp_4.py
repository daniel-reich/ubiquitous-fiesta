
def shift_letters(txt, n):
  lst=[c for c in txt if c.isalpha()]
  n=n%len(lst)
  lst=lst[-n:]+lst[:-n]
  return ''.join(lst.pop(0) if c.isalpha() else c for c in txt)

