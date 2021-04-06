
def is_slidey(n):
  return all([int(i[0])-int(i[1]) in [-1,1] for i in zip(str(n),str(n)[1:])])

