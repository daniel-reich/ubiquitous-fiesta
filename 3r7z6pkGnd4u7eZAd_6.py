
def mark_maths(lst):
  a = [i.split('=') for i in lst]
  b = sum([1 for x, y in a if eval(x)==int(y)])
  
  return '{}%'.format(round((b / len(lst)) * 100))

