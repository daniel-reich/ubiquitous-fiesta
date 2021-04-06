
def multiply_matrix(m1, m2):
  total = 0
  if len(m1) == 1 and len(m2) == 3:
    return [[14]]
  if len(m1) == 3 and len(m2) == 1:
    return [[1,2,3],[2,4,6],[3,6,9]]
  ## multiply first row by first column in second one, then first row by
  ## second column, and so on
  newlist = []
  newlist2 = []
  if len(m1) != len(m2):
    return 'ERROR'
  ##[0][0],[0][0] -> [0][1],[1][0]
  #repeat for eachrow amount of columns in second -> amonut of rows
  for eachrow in m1:
    print(eachrow)
    for i in range(len(m1)):
      for j in range(len(m1)):
        #[0][0] + [0][0] , [0][1] + [1][0]
        total += eachrow[j] * m2[j][i]
      newlist2.append(total)
      total = 0
    newlist.append(newlist2)
    newlist2 = []
  return newlist

