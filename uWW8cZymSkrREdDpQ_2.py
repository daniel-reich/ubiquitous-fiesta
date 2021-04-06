
def sums_up(lst):
  ans = {}
  s = set()
  sub = []
  for i in range(len(lst)):
    d = 8 - lst[i]
    if d in lst and lst.index(d) != i:
      if max(lst.index(d), i) in ans and (d not in s and lst[i] not in s):
        ans[max(lst.index(d), i)].append(sorted([d, lst[i]]))
      else:
        s.add(d)
        s.add(lst[i])
        ans[max(lst.index(d), i)] = [sorted([d, lst[i]])]
  for i in sorted(ans.keys()):
    for j in ans[i]:
      sub.append(j)
  return {'pairs': sub}

