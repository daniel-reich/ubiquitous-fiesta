
def party_people(lst):
  l = len(lst)
  nlst = []
  for p in lst:
    if p <= l: nlst.append(p)
  if lst == nlst: return l
  return party_people(nlst)

