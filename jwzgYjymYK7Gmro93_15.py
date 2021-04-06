
def get_indices(lst, el):
  return [
    index
    for index, element in enumerate(lst)
    if element == el
  ]

