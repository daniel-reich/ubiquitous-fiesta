
def subtract_matrix(lst1, lst2):
  newlist = []
  newlist2 = []
  for i in range(len(lst1)):
    for j in range(len(lst2)):
      #[0][0],[0][1],[0][2]
      if type(lst1[i][j]) is str:
        lst1[i][j] = int(lst1[i][j])
      if type(lst2[i][j]) is str:
        lst2[i][j] = int(lst2[i][j])
      newlist2.append(lst1[i][j] - lst2[i][j])
    newlist.append(newlist2)
    newlist2 = []
  return newlist

