
def reverse_sort(s):
  r, s = [], sorted(s.split(), key=len)[::-1]
  while len(s):
    if len(r) and len(r[-1][-1]) == len(s[0]): r[-1] += [s[0]]
    else: r += [[s[0]]]
    s = s[1:]
  return ' '.join([' '.join(reversed(sorted(x, key=str.casefold))) for x in r])

