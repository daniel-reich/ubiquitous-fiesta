
def find_the_falsehoods(lst):
  a = []
  for index in lst:
    if index == None or index == 0 or index == () or index == [] or index == {} or index == "":
      a.append(index)
  return a

