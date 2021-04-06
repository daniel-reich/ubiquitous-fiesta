
import ast
​
def resist(net):
  net = ast.literal_eval(net)
  def series(lst):
    #use for tuples
    return sum([element(i) for i in lst])
​
  def parralel(tup):
    #use for lists
    return 1/sum([1/element(i) for i in tup])
​
  def element(item):
    if type(item) == int:
      return item
    elif type(item) == tuple:
      return series(item)
    elif type(item) == list:
      return parralel(item)
  return round(element(net),1)

