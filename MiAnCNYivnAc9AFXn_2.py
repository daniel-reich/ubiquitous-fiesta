
def change_types(lst):
  return [i.capitalize()+'!' if type(i)==str else not i if type(i)==bool else i//2*2 + 1 for i in lst]

