
def get_diagonals(lst):
  left = [lst[i][i] for i,v in enumerate(lst)]
  right = [lst[::-1][i][i] for i,v in enumerate(lst)][::-1]
  return [left,right]

