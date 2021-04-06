
def reverse_sort(txt):
  final = ''
  txt = sorted(txt.split(),key=len)
  lengths = {len(i):[] for i in txt}
  for i in txt:
    lengths[len(i)].append(i)
  for i in reversed(range(min(lengths.keys()),max(lengths.keys())+1)):
    if i in lengths:
      final+=' '.join(sorted(lengths[i],key=lambda x:(x.lower(),txt[::-1].index(x)))[::-1])+' '
  return final[:-1]

