
def custom_sort(t, s):
  a, b='', ''
  for x in s:
    if x in t:
      a+=x
    else:
      b+=x
  return ''.join(sorted(a, key=lambda x: t.index(x))+sorted(b))

