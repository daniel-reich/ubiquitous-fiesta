
def bracket_logic(xp):
  bracks = {']' : '[', ')' : '(', '}' : '{', '>' : '<'}
  prevbracks = ['']
  for l in xp:
    if l in bracks and prevbracks[-1] != bracks[l]:
      return False
    elif l in bracks and bracks[l] == prevbracks[-1]:
      prevbracks.pop()
    elif l in bracks.values():
      prevbracks.append(l)
  if len(prevbracks) > 1:
    return False
  return True

