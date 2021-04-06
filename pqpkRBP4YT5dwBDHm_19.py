
def show_the_love(lst):
  love = min(lst)
  index = lst.index(love)
  result = []
  for i, j in enumerate(lst):
    if i != index:
      result.append(j * .75)
      love += j * .25
  result.insert(index, love)
  return result

