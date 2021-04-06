
def remove_repeats(s):
  l = [s[0]]
  for i in s:
    if i !=l[-1]:
      l.append(i)
  return ''.join(l)

