
def cutting_grass(lst, *cuts):
  final = []
  for i in cuts:
    if any(l == 0 for l in lst):
      final.append('Done')
    else:
      lst = [k - i for k in lst]
      if any(j == 0 for j in lst):
        final.append('Done')
      else:
        final.append(lst)
  return final

