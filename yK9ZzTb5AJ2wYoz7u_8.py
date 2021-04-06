
def floyd(up_to = None, n_row = None):
  newlist = []
  newlist2 = []
  counter = 1
  count_rows = 0
  amount_per_row = 1
  if up_to == None:
    while count_rows < n_row:
      for i in range(amount_per_row):
        newlist2.append(counter)
        counter += 1
      newlist.append(newlist2)
      amount_per_row += 1
      count_rows += 1
      newlist2 = []
    return newlist
  else:
    while up_to not in newlist2:
      for i in range(amount_per_row):
        newlist2.append(counter)
        counter += 1
      newlist.append(newlist2)
      amount_per_row += 1
      if up_to in newlist2:
        return newlist
      else:
        newlist2 = []
    print(newlist)

