
def add_letters(a):
  al = 'zabcdefghijklmnopqrstuvwxy'
  return al[sum(al.index(x) for x in a)%26 if a else 0]

