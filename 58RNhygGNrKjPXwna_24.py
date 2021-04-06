
def longest_nonrepeating_substring(txt):
  subs = []
  lens = []
  for i in range(len(txt)):
    sub = []
    while i < len(txt):
      if txt[i] not in sub:
        sub.append(txt[i])
        i += 1
      else:
        sub = ''.join(sub)
        subs.append(sub)
        lens.append(len(sub))
        sub = []
    sub = ''.join(sub)
    subs.append(sub)
    lens.append(len(sub))
  m = max(lens)
  for sub in subs:
    if len(sub) == m:
      return sub

