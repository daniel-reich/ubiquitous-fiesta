
def move_to_end(lst, el):
  return [x for x in lst if x!=el]+[el]*lst.count(el)

