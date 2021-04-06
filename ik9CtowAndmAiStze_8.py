
def frequency_sort(s):
  is_upper = [True,False]
  chars = [char for char in s]
  chars.sort()
  chars.sort(key = lambda x: is_upper.index(x.isupper()))
  chars.sort(key = lambda x: s.count(x),reverse = True)
  return ''.join(chars)

