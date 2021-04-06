
def get_missing_letters(s):
  a="abcdefghijklmnopqrstuvwxyz"
  m=""
  for n in a:
    if s.count(n)==0:
      m+=n
  return m

