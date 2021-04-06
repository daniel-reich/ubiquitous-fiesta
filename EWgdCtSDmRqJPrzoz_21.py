
def peel_layer_off(lst):
  if len(lst) >1:
    new_list=[x[1:-1] for x in lst]
    new_2=new_list[1:-1]
    return new_2
  return lst

