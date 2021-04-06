
def odd_sort(lst):
  set_odd = list()
  for i in range(len(lst)) :
    if  lst[i] % 2 == 1 : 
      set_odd.append(lst[i])
      lst[i] = "a"
  print(set_odd)
  set_odd.sort()
  print(set_odd)
  temp_c = 0 
  for j in range(len(lst)) : 
    if lst[j] == "a": 
      lst[j] = set_odd[temp_c]
      temp_c += 1
  return lst

