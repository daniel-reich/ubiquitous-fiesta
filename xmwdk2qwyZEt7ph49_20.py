
def get_length(lst):
  is_list = (lambda item:
            isinstance(item, list))
  list_items = list(filter(is_list, lst))
  if list_items == []:
    return len(lst)
  else: 
    return len(lst) - len(list_items) +     \
           sum(get_length(list_item)
               for list_item in list_items)

