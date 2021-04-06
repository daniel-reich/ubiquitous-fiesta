
def custom_sort(t, s):
  s=''.join(sorted(s))
  return ''.join(sorted(s, key=lambda x: (t+s).index(x)))

