
def possible_path(lst):
  ok = True
  dict = {"1":[2],"2":[1,"H"],"3":[4],"4":[3,"H"],"H":[2,4]}
  for i in range(len(lst)-1):
    possiblePath = dict[str(lst[i])]
    if lst[i+1] not in possiblePath:
      ok = False
  return ok

