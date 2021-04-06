
def flip_list(lst):
  if lst==[]:
    return []
  if type(lst[0])==int:
    return [[i] for i in lst]
  else:
    return [i[0] for i in lst]

