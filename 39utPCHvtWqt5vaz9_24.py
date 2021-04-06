
def direction(lst):
  lst = [word.replace('e', 'w') for word in lst]
  lst = [word.replace('E', 'W') for word in lst]
  lst = [word.replace('a', 'e') for word in lst]
  lst = [word.replace('A', 'E') for word in lst]
  return lst

