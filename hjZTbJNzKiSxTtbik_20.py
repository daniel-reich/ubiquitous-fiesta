
def sort_by_string(lst, txt):
  temp = sorted([(txt.index(i[0]),i) for i in lst])
  return [i[1] for i in temp]

