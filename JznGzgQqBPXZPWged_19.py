
from ast import literal_eval
​
is_series = lambda r : isinstance(r, tuple)
is_parallel = lambda r : isinstance(r, list)
is_resist = lambda i : is_series(i) or is_parallel(i)
​
def _calc(net):
  count = 0
  for i in net:
    if is_resist(i):
      i = _calc(i)
    count += i ** (-1 * is_parallel(net) or 1)
  return count ** (-1 * is_parallel(net) or 1)
​
def resist(net):
  return round(_calc(literal_eval(net)), 1)

