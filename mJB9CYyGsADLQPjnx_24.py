
def first_non_repeated_character(txt):
  if len(txt) == 0: return False
  txt = txt.lower()
  cnt = {}
  for c in txt:
    if c in cnt:
      cnt[c] += 1
    else:
      cnt[c] = 1
  for c in txt:
    if cnt[c] == 1:
      return c
  return False

