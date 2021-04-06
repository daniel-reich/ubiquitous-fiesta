
def reverse_sort(txt):
  f = lambda x: (len(x),x.lower(),-ord(x[0]))
  return ' '.join(sorted(txt.split(),key=f)[::-1])

