
def cumulative_sum(lst):
  current =0
  new = []
  for n in lst:
    current += n
    new.append(current)
  return new

