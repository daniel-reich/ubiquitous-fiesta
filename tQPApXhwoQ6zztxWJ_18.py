
def get_prices(lst):
  final = []
  for s in lst:
    final.append(float(s.partition('($')[2].partition(')')[0]))
  return final

