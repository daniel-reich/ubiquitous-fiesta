
def clean_up_list(lst):
  return [[int(x) for x in lst if int(x) % 2 == 0], [int(y) for y in lst if int(y) % 2 != 0]]

