
def rotate(mat):
  newlist = []
  newlist2 = []
  for i in range(len(mat)):
    for eachlayer in mat[::-1]:
      newlist2.append(eachlayer[i])
    newlist.append(newlist2)
    newlist2 = []
  return newlist

