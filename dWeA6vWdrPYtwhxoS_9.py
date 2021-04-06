
def count_number(lst):
  lst = str(lst).replace('[',' ').replace(']',' ').replace(',',' ').replace('.','').split()
  lst = [i for i in lst if i.isdigit()]
  return len(lst)

