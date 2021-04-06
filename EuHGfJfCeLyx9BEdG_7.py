
def party_people(lst):
  lst=sorted(lst)
  if lst:
    if lst[-1]<=len(lst):
      return len(lst)
    else:
      return party_people(lst[:-1])
  else:
    return 0

