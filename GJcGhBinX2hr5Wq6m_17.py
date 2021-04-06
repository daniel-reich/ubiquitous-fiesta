
def move_zeros(lst):
  non_zeros = [i for i in lst if i != 0 or type(i) == bool] 
  number_of_zeros =  len(lst) -len(non_zeros)
  return non_zeros + [0] * number_of_zeros

