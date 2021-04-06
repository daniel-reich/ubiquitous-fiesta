
def digit_sort(lst):
  return sorted(sorted(lst), key=lambda num: len(str(num)), reverse=True)

