
def num_of_sublists(lst):
  list_string = str(lst)
  list_string2 = list_string[1:len(list_string) - 1]
  count = 0
  for i in range(0, len(list_string2)):
    if list_string2[i] == "[":
      count+=1
  return count

