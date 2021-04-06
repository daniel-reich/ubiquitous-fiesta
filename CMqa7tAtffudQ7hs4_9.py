
def sorting_steps(lst):
  temp_lst = [x for x in lst]
  result = []
  while temp_lst != sorted(temp_lst):
    for i in range(len(temp_lst)-1):
      if temp_lst[i] > temp_lst[i+1]:
        temp_lst[i], temp_lst[i+1] = temp_lst[i+1], temp_lst[i]
        result.append([i, i+1])
        break
  return result

