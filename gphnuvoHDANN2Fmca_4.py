
def odd_sort(lst):
  os = sorted([i for i in lst if i%2])
  return [os.pop(0) if i%2 else i for i in lst]

