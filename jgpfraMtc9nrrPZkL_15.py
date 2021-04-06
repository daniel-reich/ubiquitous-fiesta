
def switch_gravity_on(lst):
  c_count = []
  for i in range(len(lst[0])):
    c_count.append(sum(row[i] == '#' for row in lst))
​
  new_lst = []
  for i, row in enumerate(lst):
    new_row = []
    for col in c_count:
      new_row.append('#') if col > i else new_row.append('-')
    new_lst.insert(0, new_row)
​
  return new_lst

