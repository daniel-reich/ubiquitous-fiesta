
def possible_path(lst):
  prev = ''
  for step in lst:
    s = 'h' if step == 'H' else 'r'
    if s == prev:
      return False
    prev = s
  return True

