
def cutting_grass(lst, *cuts):
  final = []
  for i in cuts:
    lst = [0 if j-i<1 else j-i for j in lst]
    if 0 in lst:
      final.append('Done')
    else:
      final.append(lst)
  return final

