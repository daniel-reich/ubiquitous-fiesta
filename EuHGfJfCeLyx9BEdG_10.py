
def party_people(lst):
  lst.sort()
  if len(lst)==0:
    return 0
  if lst[-1]>len(lst):
    return party_people(lst[:-1])
  return len(lst)

