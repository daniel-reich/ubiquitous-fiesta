
def change_types(lst):
  return [(i + "!").capitalize() if type(i) == str else i + 1 if type(i) == int and i % 2 == 0 else False if i == True else True if i == False else i for i in lst]

