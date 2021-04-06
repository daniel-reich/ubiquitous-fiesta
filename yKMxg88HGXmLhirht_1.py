
def add_letters(lst):
  al = 'zabcdefghijklmnopqrstuvwxy'
  return al[sum(al.index(l) for l in lst)%26]

