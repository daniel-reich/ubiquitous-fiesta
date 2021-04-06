
def digit_sort(lst):
  return sorted(sorted(lst), key=lambda x:len(str(x)), reverse=True)

