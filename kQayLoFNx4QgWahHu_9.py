
def order(lst):
  return [i[1] for i in sorted([[x, j] for j, x in enumerate(lst)])]

