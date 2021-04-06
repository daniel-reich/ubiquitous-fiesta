
def stem_plot(lst):
  lst2 = sorted(lst)
  stems = [num // 10 for num in lst2]
  leaves = [num % 10 for num in lst2]
  
  plots = {}
  
  for stem, leaf in zip (stems, leaves):
    if plots.get(stem) == None:
      plots[stem] = [leaf]
    else:
      plots[stem].append(leaf)
    
  newlist = [str(stem) + " |" + ''.join([" " + str(leaf) for leaf in plots[stem]]) for stem in stems]
  news = []
  for new in newlist:
    if not new in news:
      news.append(new)
  return news

