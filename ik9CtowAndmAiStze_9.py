
def frequency_sort(s):
  lst={ x:(-s.count(x), x==x.lower(),x ) for x in set(s) }
  return ''.join(sorted(s,key=lambda x:lst[x]))

