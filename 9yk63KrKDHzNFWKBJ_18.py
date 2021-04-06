
def is_it_inside(folders,X,Y):
  above_X, current = [X], X
  while True:
    previous = [Z for Z in folders if current in folders[Z]]
    if previous:
      above_X+= [previous[0]]
      current = previous[0]
    else: return Y in above_X

