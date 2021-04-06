
def make_transpose(m):
  #grab columns, transfer to list
  newlist = []
  modified_row = []
  for i in range(len(m[0])):
    for j in range(len(m)):
      modified_row.append(m[j][i])
    newlist.append(modified_row)
    modified_row = []
  return newlist

