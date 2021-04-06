
def party_people(lst):
  lst_after_leaves = [i for i in lst if i <= len(lst)]
  if lst == lst_after_leaves:
    return len(lst)
  else:
    return party_people(lst_after_leaves)

