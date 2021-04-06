
def three_sum(lst):
  import itertools
  output = []
  for n in itertools.combinations(lst, 3):
    n = list(n)
    if n[0]+n[1]+n[2]==0 and n not in output:
      output.append(n)
  return output

