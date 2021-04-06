
def pos_neg_sort(lst):
  positives = iter(sorted(i for i in lst if i > 0))
  return [next(positives) if i > 0 else i for i in lst]

