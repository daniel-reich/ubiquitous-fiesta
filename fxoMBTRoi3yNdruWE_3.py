
def in_box(lst):
  for word in lst[1:-1]:
    for c in word:
      if c=='*':
        return True
  return False

