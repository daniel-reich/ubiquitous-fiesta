
def sort_array(lst):
  return [lst.pop(lst.index(min(lst))) for i in range(len(lst))]

