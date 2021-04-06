
def move_to_end(lst, el):
  return  [item for item in lst if item != el]+[item for item in lst if item == el]

