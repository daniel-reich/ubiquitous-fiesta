
def add_it_up(lst):
  types = {
    list: [],
    tuple: tuple(),
    int: 0,
    float: 0.
  }
  return sum(lst, types[type(lst[0])])

