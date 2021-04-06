
def alternate_sort(lst):
  a,b = [i for i in lst if type(i)==int],[i for i in lst if type(i)==str]
  return list(sum(zip(sorted(a),sorted(b)),()))

