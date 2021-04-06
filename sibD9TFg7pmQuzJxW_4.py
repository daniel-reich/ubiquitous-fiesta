
def stem_plot(lst):
  lst = sorted(lst)
  stems = sorted(list(set([i//10 for i in lst])))
  stems = [[i,[]] for i in stems]
  for i in range(len(stems)):
    for x in lst:
      if x//10 == stems[i][0]:
        stems[i][1].append(x%10)
    stems[i][1] = sorted(stems[i][1])
    stems[i] = str(stems[i][0]) + ' | ' + ' '.join([str(a) for a in stems[i][1]])
  return stems

