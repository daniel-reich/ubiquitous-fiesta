
def str_to_dict(lst):
  my_dict = {}
  for i in lst:
    my_dict[i.split('=')[0]] = i.split('=')[1]
  
  return my_dict

