
def count_towers(towers):
  return max([len(j.split()) for i in towers for j in i])

