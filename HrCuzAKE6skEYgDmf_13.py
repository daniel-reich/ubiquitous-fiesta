
def pairs(lst):
  p = len(lst) // 2
  return [[lst[i], lst[-(i + 1)]] for i in range([p, p + 1][len(lst) % 2])]

