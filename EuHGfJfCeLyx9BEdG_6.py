
def party_people(lst):
  p = [i for i in lst if i <= len(lst)]
  return len(lst) if len(lst) == len(p) else party_people(p)

