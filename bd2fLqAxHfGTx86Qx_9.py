
def can_complete(initial, word):
  for i in word:
    if initial[0] == i:
      initial = initial[1:]
  return True if len(initial) == 0 else False

