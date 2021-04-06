
import math
def asci(char):
  if type(char) != str:
    char = str(char)
  return sum(list(map(lambda x: ord(x),char)))
  
def pairwise_swap(list_of_elements):
  if not list_of_elements:
    return []
  elif None in list_of_elements:
    return [None]
  else:
    for i in range(0,len(list_of_elements)-1,2):
      list_of_elements[i],list_of_elements[i+1] = list_of_elements[i+1],list_of_elements[i]
    if len(list_of_elements) % 2 == 1:
      lst = list(map(lambda x: asci(x),list_of_elements))
      index = lst.index(max(lst))
      list_of_elements[-1],list_of_elements[index] = list_of_elements[index],list_of_elements[-1]
    return list_of_elements

