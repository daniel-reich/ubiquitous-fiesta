
def custom_sort(t, s):
  if t == '': return ''.join(sorted(s))
  res1 = ''.join(sorted([i for i in s if i in t], key=lambda x: t.index(x)))
  res2 = ''.join(sorted([i for i in s if i not in t]))
  result = res1 + res2
  return result

