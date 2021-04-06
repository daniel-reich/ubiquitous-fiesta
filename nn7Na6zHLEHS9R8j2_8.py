
def deep_count(lst):
  S=len(lst)
  for element in lst:
    if type(element)==list:
      S+=deep_count(element)
  return S

