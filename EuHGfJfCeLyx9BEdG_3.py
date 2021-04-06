
def party_people(lst):
  
  is_good = lambda safe: lambda lst: len(lst) >= safe
  
  ppl = {n:is_good(lst[n]) for n in range(len(lst))}
  
  ready = True
  to_remove = []
  
  for i in ppl.keys():
    person = ppl[i]
    if person(lst) == False:
      ready = False
      to_remove.append(i)
  
  for i in reversed(sorted(to_remove)):
    lst.pop(i)
  
  if ready == True:
    return len(lst)
  else:
    return party_people(lst)

