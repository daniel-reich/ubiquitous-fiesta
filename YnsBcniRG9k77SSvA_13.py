
def print_all_groups():
  list = []
  list2 =", "
  years = [1,2,3,4,5,6]
  groups = ["a","b","c","d","e"]
  for year in years:
    for group in groups:
      list.append(str(year)+group)
  return (list2.join(list))

