
def count_towers(towers):
  count = 0
  for ch in towers[len(towers)-1][0]:
    if(ch == '#'):
      count += 1
  return count//2

