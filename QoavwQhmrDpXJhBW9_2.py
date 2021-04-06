
def flip_list(lst):
  if lst==[]: return []
  if not isinstance(lst[0],list):
    return [[i] for i in lst]
  else:
    return [i[0] for i in lst]

