
def move_to_end(lst, el):
  return [x for x in lst if x!=el]+[y for y in lst if y==el ]

