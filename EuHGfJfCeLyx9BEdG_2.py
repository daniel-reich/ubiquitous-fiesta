
def party_people(lst):
  if not lst:
    return 0
  removed = 0
  people = len(lst)
  new_lst = []
  while lst:
    if lst[0] > people:
      people -= 1
      removed += 1
    else:
      new_lst.append(lst[0])
    lst.pop(0)
  if removed == 0:
    return people
  return party_people(new_lst)

