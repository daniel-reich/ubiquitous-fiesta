
def change_types(lst):
  for x in range(len(lst)):
    if lst[x] == True:
      lst[x] = False
    elif lst[x] == False:
      lst[x] = True
    elif type(lst[x]) == str:
      lst[x] = lst[x].title() + '!'
    elif type(lst[x]) == int:
      if lst[x]%2 == 0:
        lst[x] += 1
  return lst

