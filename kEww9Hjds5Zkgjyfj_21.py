
def replace_next_largest(lst):
  final = []
  used = []
  for i in range(len(lst)):
    if max(lst) == lst[i]:
      final.append(-1)  
    for j in sorted(lst):
      if j > lst[i] and j not in used:
        final.append(j)
        used.append(j)
        break
  return final

