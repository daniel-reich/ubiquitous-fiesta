
def sums_up(lst):
  def adds_to_8(n, lst):
    if 8-n in lst and n*2 != 8:
      return sorted([n, 8-n])
    else:
      return False
  def settify(lst):
    sett = []
    for item in lst:
      if item not in sett:
        sett.append(item)
    return sett
  def position(pair, lst):
    positions = []
    for n in range(len(lst)):
      num = lst[n]
      if num in pair:
        positions.append(n)
    return max(positions)
  
  all_pairs = []
  
  for n in lst:
    tst = adds_to_8(n, lst)
    if tst != False:
      all_pairs.append(tst)
# print(all_pairs)
  all_pairs = settify(all_pairs)
  
  positions = {}
  
  for pair in all_pairs:
    positions[position(pair, lst)] = pair
  
  all_pairs = [positions[position] for position in sorted(list(positions.keys()))]
# print(sorted(list(positions.keys())), positions)
  return {'pairs': all_pairs}

