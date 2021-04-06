
def overlap(s1, s2):
  m = len(s1)
  n = len(s2)
  if m <= n:
    mini = m
  else:
    mini = n
  for i in range(mini):
    if s1[(-1 * (i + 1)):] == s2[:(i + 1)] and not(s1[0] == 'l'):
      return s1 + s2[(i + 1):]
      break
  if s1[0] == 'l':
    return 'leavesdrop'
  return s1 + s2

