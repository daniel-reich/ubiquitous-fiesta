
def is_apocalyptic(number):
  desc = ['Safe','Single','Double','Triple']
  occ = str(2 ** number).count('666')
  return desc[occ]

