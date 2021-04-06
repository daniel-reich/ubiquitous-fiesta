
def swap(txt, i, j):
  chrs = list(txt)
  chrs[i], chrs[j] = chrs[j], chrs[i]
  return ''.join(chrs)
​
def maxmin(n):
  ns = str(n)
  # maxie:
  # for each digit in turn
  #   if largest following digit > current
  #     swapit -> maxie
  minie = maxie = n
  for i in range(len(ns)-1):
    rest = ns[i+1:]
    j = ns.rindex(max(rest))
    if ns[j] > ns[i]:
      maxie = int(swap(ns, i, j))
      break
  # minie:
  # for each digit in turn
  #   if smallest following digit < current (if current is 1st exclude 0 from min search)
  #     swapit -> minie
  for i in range(len(ns)-1):
    rest = ns[i+1:]
    if int(rest) == 0:
      break
    j = ns.rindex(min(rest) if i > 0 else min(rest.replace('0','')))
    if ns[j] < ns[i]:
      minie = int(swap(ns, i, j))
      break
  return (maxie, minie)

