
def peel_layer_off(lst):
  return [
    [inner 
    for inner in outer[1:-1]]
    for outer in lst[1:-1]
    
  ]

