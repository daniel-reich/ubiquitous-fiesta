
def party_people(lst):
  if all([i<=len(lst) for i in lst]):
    return len(lst)
  return party_people([i for i in lst if i<=len(lst)])

