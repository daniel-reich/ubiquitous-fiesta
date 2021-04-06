
def final_result(lst):
  output_lst = []
  
  b = True
  while b:
    i = 0
    indexes_to_delete = []
    prev_item = ""
    next_item = ""
    current_item = ""
    for item in lst:
      if (i == 0 and len(lst) > 1):
        current_item = lst[i]
        next_item = lst[i+1]
        prev_item = ""
      elif (i > 0 and i < len(lst) - 1):
        current_item = lst[i]
        prev_item = lst[i-1]
        next_item = lst[i+1]
      elif (len(lst) > 1):
        current_item = lst[i]
        prev_item = lst[i-1]
        next_item = ""
​
      if (current_item == prev_item and len(lst) > 1):
        if (i not in indexes_to_delete):
          indexes_to_delete.append(i)
        if (i-1 not in indexes_to_delete):
          indexes_to_delete.append(i-1)
      elif (current_item != prev_item and len(indexes_to_delete) > 0):
        break
      i = i + 1
​
    list1 = []
    if (len(indexes_to_delete) > 0):
      for i in range(len(lst)):
        if (i not in indexes_to_delete): 
          list1.append(lst[i])
      lst = list1
      b = True
    else:
      b = False
  
  return lst

