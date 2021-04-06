
def grouping(w):
  final = {}
  res = [[sum(j.isupper() for j in i), i] for i in w]
  for i in res:
    if i[0] not in final:
      final[i[0]] = [i[1]]
    else:
      final[i[0]].append(i[1])
  [final[i].sort(key=lambda s: s.lower()) for i in final]
  print(final)
  return final

