
def sort_array(lst):
  slst = []
  while True:
    slst.append(min(lst))
    lst.remove(min(lst))
    if lst == []:
      return slst

