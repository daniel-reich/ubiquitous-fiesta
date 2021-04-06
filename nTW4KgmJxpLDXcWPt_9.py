
def move_to_end(lst, el):
   return [i for i in lst if i != el] + [i for i in lst if i == el]

