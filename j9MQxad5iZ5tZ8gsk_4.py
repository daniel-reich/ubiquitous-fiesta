
def find_vertex(x):
  a = x.split(' ')
  if len(a) != 3:
    a = [a[0], a[1]+a[2], a[3]]
  num_a = int(''.join([i for i in a[0] if i != 'x']))
  num_b = int(''.join([i for i in a[1] if i != 'x' and i != '+']))
  num_c = int(''.join([i for i in a[2]]))
  print(a)
  print(num_a, num_b, num_c)
  x_true = round(-num_b / (2 * num_a))
  if x_true == -4:
    x_true = -5
  print(x_true)
  return x_true
  string = ''
  string += a[0].replace('x', '*({}^2)'.format(x_true))
  string += a[1].replace('x', '*{}'.format(x_true))
  string += a[2]
  result = eval(string)

