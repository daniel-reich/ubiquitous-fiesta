
def move_zeros(lst):
  return [i for i in lst if str(i) not in ['0', '0.0']] + [j for j in lst if str(j) in ['0', '0.0']]

