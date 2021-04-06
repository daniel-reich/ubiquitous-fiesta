
def show_the_love(lst):
  result = []
  add = 0
  for i in range(0, len(lst)):
    if lst[i]!=min(lst):
      if (lst[i]*0.75)%1 == 0:
        result.append(int(lst[i]*0.25))
      else:
        result.append(lst[i]*0.25)
    else:
      result.append(0)
  final = []
  for j in range(0, len(lst)):
    if result[j] != 0:
      final.append(lst[j]-result[j])
    else:
      final.append(lst[j]+sum(result))
  return final

