
def stem_plot(lst):
  lst.sort();res=['']
  for i in lst:
    i='{:0>2}'.format(i)
    if i[:-1]+' |' in res[-1]:
      res[-1]+=' '+i[-1]
    else:
      res+=[i[:-1]+' | '+i[-1]]
  return res[1:]

