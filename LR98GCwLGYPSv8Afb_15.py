
def pluralize(lst):
  return dict.fromkeys([ i if lst.count(i) == 1 else i+"s" for i in lst ]).keys()

