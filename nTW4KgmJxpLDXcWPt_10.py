
def move_to_end(lst, el):
  lst1= [x for x in lst if x!=el]
  lst2= [x for x in lst if x==el]
  return lst1+lst2

