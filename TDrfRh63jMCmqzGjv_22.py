
def is_anti_list(lst1, lst2):
  list_transform = transform(lst1)
  return list_transform == lst2
​
def transform(lst1):
  unique_elements = list(set(lst1))
  response = []
  for element in lst1:
    add_element = unique_elements[1] if element == unique_elements[0] else unique_elements[0]
    response.append(add_element)
  return response

