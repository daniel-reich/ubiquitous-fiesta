
def diag_dom(lst):
  lst = [[abs(number) for number in i] for i in lst]
  for index , item in enumerate(lst):
    if lst[index][index] <= sum(item) - lst[index][index]:
      return False
  return True

