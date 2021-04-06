
def move_to_end(lst, el):
  return [i for i in lst if i!=el]+([el]*lst.count(el))

