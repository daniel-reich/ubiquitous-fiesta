
def stem_plot(lst):
  lst = [str(i) if i > 9 else '0'+str(i) for i in lst]
  dic = {}
  for i in lst:
    stem, leaf = i[:-1], i[-1]
    if stem not in dic: 
      dic[stem] = []
    dic[stem] += [leaf]
  return ['{} | {}'.format(k, ' '.join(sorted(v))) for k, v in sorted(dic.items(), key=lambda x: int(x[0]))]

