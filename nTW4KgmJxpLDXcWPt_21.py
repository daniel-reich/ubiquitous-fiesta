
def move_to_end(lst, el):
  return [e for e in lst if e!=el]+[e for e in lst if e==el]

