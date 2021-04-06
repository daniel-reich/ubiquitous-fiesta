
def can_complete(initial, word):
  start=0
  for l in initial:
    if l in word[start:] and initial.count(l)<=word.count(l):
      start=word.find(l,start)
    else:
      return False
  return True

