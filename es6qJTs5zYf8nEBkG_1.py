
def is_rectangle(coordinates):
  lst = [x.replace(" ", "").split(',') for x in coordinates]
  x = [x[0][-2:] if x[0][-2] == '-' else x[0][-1] for x in lst]
  y = [x[1][:2] if x[1][0] == '-' else x[1][0] for x in lst]
  return all([sum([x[j] == x[i] for j in range(len(x))]) == sum([y[j] == y[i] for j in range(len(y))]) == 2
        for i in range(len(x))])

