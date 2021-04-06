
def difference_two(lst):
  final = []
  lst = sorted(lst)
  for i in range(len(lst)):
    for j in range(i,len(lst)):
      if abs(lst[i]-lst[j]) == 2:
        final.append([lst[i],lst[j]])
  return final

