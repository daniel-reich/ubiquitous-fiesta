
def is_ord_sub(smlst, biglst):
  sub_counter = 0
  current_index = 0
  startIndex = 0
  for i in smlst:
    for j in biglst[startIndex:]:
      if i == j:
        startIndex = current_index
        sub_counter += 1
        current_index += 1
        break
​
      current_index += 1
  
  return sub_counter == len(smlst)

