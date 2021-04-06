
def peel_layer_off(lst):
  lst.pop(0)
  lst.pop()
  
  [item.pop(0) for item in lst]
  [item.pop() for item in lst]
  return lst

