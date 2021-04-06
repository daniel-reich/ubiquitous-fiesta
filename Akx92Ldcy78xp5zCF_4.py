
def custom_sort(t, s):
​
  return ''.join(sorted(list(s), key=lambda x: t.index(x) if x in t else ord(x) ))

