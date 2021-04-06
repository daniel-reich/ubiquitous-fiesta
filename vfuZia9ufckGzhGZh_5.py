
def seq_level(lst):
  cd = (lst[2] - lst[1]) - (lst[1]-lst[0])
  if((lst[0]-lst[1])==1 or (lst[0]-lst[1])==-1):return 'Linear'
  if((lst[3]-lst[2]) - (lst[2]-lst[1]) ==cd):return 'Quadratic'
  return 'Cubic'

