
def flip_list(lst):
  return [] if lst==[] else [i[0] for i in lst] if type(lst[0]) is list else [[i] for i in lst]

