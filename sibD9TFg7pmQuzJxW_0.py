
def stem_plot(lst):
  lst = [str(i) if len(str(i)) > 1 else '0'+str(i) for i in lst]
  stems = sorted(list(set(i[:-1] for i in lst)),key=lambda x:int(x))
  return [' | '.join([i,' '.join(sorted([j[-1] for j in lst if j[:-1] == i]))]) for i in stems]

