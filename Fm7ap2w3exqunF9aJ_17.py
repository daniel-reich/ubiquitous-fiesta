
def count_lone_ones(n):
  parts = [ [ str(n)[0] ] ]
  for i in str(n)[1:]:
    if i in parts[-1]: parts[-1] += i
    else: parts.append([i])
  return sum(1 for p in parts if p == ['1'])

