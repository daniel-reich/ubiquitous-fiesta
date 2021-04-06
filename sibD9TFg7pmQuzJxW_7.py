
def stem_plot(lst):
  rep, plt = [], {}
  for n in lst:
    s = str(n)
    stem, leaf = int(s[:-1] or 0), int(s[-1]) 
    if stem not in plt:
      plt[stem] = []
    plt[stem].append(leaf)
    
  for stem in sorted(plt.keys()):
    leaves = ' '.join(map(str, sorted(plt[stem])))
    rep.append('{} | {}'.format(stem, leaves))
  
  return rep

