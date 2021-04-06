
def char_at_pos(r, s):
  if s == 'even':
    i = [r[i] for i in range(len(r)) if (i + 1) % 2 == 0]
  else:
    i = [r[i] for i in range(len(r)) if (i + 1) % 2 != 0]
  return i if type(r) == list else ''.join(i)

