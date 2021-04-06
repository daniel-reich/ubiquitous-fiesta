
def stem_plot(lst):
  nums = [str(x) if x >= 10 else '0' + str(x) for x in lst]
  pairs = {}
  for x in nums:
    stem, leaf = x[:-1], x[-1]
    if stem not in pairs:
      pairs[stem] = [leaf]
    else:
      pairs[stem] += [leaf]
  plot = []
  for stem in sorted(pairs.keys(), key=int):
    leaves = [str(x) for x in sorted(pairs[stem], key=int)]
    plot.append(stem + ' | ' + ' '.join(leaves))
  return plot
      
  
  
  stem_leaf_pairs = {x[:-1]: x[-1] for x in nums}

