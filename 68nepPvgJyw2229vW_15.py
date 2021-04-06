
def pairwise_swap(list_of_elements):
  if len(list_of_elements) % 2 == 0:
    swapped_list = []
    for i in range(0, len(list_of_elements), 2):
      swapped_list += list(reversed(list_of_elements[i:i+2]))
    return swapped_list
  else:
    if len(list_of_elements) == 1:
      return list_of_elements
    last_element = list_of_elements[-1]
    list_of_elements = pairwise_swap(list_of_elements[:-1])
    ord_list = [list(str(i)) for i in list_of_elements]
    ord_list = [sum([ord(j) for j in i]) for i in ord_list]
    ascii_max_location = 0
    for i in range(1, len(ord_list)):
      if ord_list[i] > ord_list[ascii_max_location]:
        ascii_max_location = i
    if ord_list[ascii_max_location] > sum([ord(i) for i in list(str(last_element))]):
      list_of_elements.append(list_of_elements[ascii_max_location])
      list_of_elements[ascii_max_location] = last_element
    else:
      list_of_elements.append(last_element)
    return list_of_elements

