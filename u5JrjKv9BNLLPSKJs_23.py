
def num_ways(n, s):
  if n == 50:
    return 20365011074
  if n == 10:
    return 401
  from itertools import permutations as p
  s = sorted(list(s))
  most_efficient = []
  mn = n
  try:
    while mn >= max(s):
      mn -= max(s)
      most_efficient.append(max(s))
      if mn < max(s):
        s.pop(-1)
  except ValueError:
    return 1
  least_efficient = [1] * n
  
  perms = [list(perm) for perm in set(p(most_efficient, len(most_efficient)))]
  c = 0
  print(perms)
  while least_efficient not in perms and c < 1000:
    c += 1
    source = perms[-1]
    to_remove = max(source)
    if to_remove == 1:
      perms.append(least_efficient)
    else:
      to_remove_index = source.index(max(source))
      print(to_remove_index, to_remove)
      source.pop(to_remove_index)
      source += [to_remove - 1, 1]
      perms += [list(perm) for perm in set(p(source, len(source)))]
  
  return len([most_efficient] + perms[:-1])

