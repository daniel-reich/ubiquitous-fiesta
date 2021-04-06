
def empty_values(lst):
  l = {int:0, float:0, list:[], str: "", bool:False, dict: {}, set:set(), tuple:()}
  return [l[type(i)] if i!= None else i for i in lst]

