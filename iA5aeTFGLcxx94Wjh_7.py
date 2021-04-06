
def delete_occurrences(lst, num):
  item_count_list = []
  items_set = set(lst)
  for item in items_set:
    item_count_list.append([item, 0])
  delete_indices = []
  for x, i in enumerate(lst):
    item_count_index = [idx for idx, val in enumerate(item_count_list) if val[0] == i][0]
    item_count_list[item_count_index][1] += 1
    if item_count_list[item_count_index][1] > num:
      delete_indices.insert(0, x)
  for index in delete_indices:
    del lst[index]
  return lst

