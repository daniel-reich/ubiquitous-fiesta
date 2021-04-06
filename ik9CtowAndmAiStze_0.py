
def frequency_sort(s):
  f={x:s.count(x)for x in sorted(s)}
  return''.join(sorted(s,key=lambda x:(-f.get(x),x)))

