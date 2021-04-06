
def sliding_sum(lst, n, k):
  l = lst
  final =[]
  for a in range(len(l)):
    sum = 0
    s = l[a:a+n]
    for a in s:
      sum = sum + a
    if sum == k:
      final.append(s)
  return final

