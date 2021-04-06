
def first_and_last(s):
  
  first = ''.join(sorted(list(s)))
  last = ''.join(sorted(list(s),reverse=True))
  lst = [first,last]
  return lst

