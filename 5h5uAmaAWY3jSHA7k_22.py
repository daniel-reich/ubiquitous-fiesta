
def landscape_type(lst):
  largest = max(lst)
  smallest = min(lst)
  peak = 0
  trough = 0
  left = []
  right = []
  if largest != lst[0] and largest != lst[-1] and lst.count(largest) == 1:
    peak = largest   # must be unique and not on boundaries in order to qualify as a peak
  if smallest != lst[0] and smallest != lst[-1] and lst.count(smallest) == 1:
    trough = smallest   # must be unique and not on boundaries in order to qualify as trough
  if peak == largest:   # confirmed peak, check if it is a mountain
    left = lst[0 : lst.index(peak)]
    right = lst[ lst.index(peak) :]
    if left == sorted(left) and right == sorted(right, reverse=True):
      return 'mountain'
  if trough == smallest:   # confirmed trough, check if it is a valley
    left = lst[0 : lst.index(trough)]
    right = lst[lst.index(trough) :]
    if left == sorted(left, reverse=True) and right == sorted(right):
      return 'valley'
  return 'neither'

