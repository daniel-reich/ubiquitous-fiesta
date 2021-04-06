
def mark_maths(lst):
  initial = [int(x[int(x.find('=') + 1):]) for x in lst]
  cut_off = [x[:int(x.find('='))] for x in lst]
  evaluated = [eval(x) for x in cut_off]
  final = []
  for a, b in zip(initial, evaluated):
    if a == b:
      final.append(a)
  return '{}%'.format(round(len(final) / len(lst) * 100))

