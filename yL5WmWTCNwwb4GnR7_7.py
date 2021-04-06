
def return_unique(lst):
  output =[]
  for number in lst:
    if lst.count(number) == 1:
      output.append(number)
  return output

