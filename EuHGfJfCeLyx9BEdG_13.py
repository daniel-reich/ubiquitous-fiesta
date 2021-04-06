
def party_people(lst):
  pers=len(lst)
  if pers==0 or max(lst)<=pers:return pers
  return party_people([x for x in lst if x<=pers])

