
def count_towers(towers):
  if len(towers[-1][0])==0:
    return 0
  return sum(1 for i in towers[-1][0].split('  '))

