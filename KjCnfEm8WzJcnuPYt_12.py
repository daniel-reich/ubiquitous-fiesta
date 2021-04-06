
def zero_indices(lst, k):
  start_point, index, maximum = 0, [], 0
  for num in range(start_point, len(lst)):
    temp_list = [x for x in lst]
    for change in range(k):
      try: temp_list[temp_list.index(0, num)] = 1
      except ValueError: break
    temp_list2 = "".join([str(x) for x in temp_list]).split("0")
    if max([len(x) for x in temp_list2]) > maximum:
      maximum = max([len(x) for x in temp_list2])
      index = [x for x in range(len(lst)) if str(lst[x]) != str(temp_list[x])]
  return index

