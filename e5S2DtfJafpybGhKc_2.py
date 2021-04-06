
def rotate(mat):
  outputlist = [[] for sublist in mat]
​
  elementcount = 0
  for sublist in mat:
      for element in sublist:
          elementcount += 1
  indexcount = len(mat) - 1
  check = 0
​
  templist = []
  for number in range(1, elementcount + 1):
      if number % len(mat) == 0:
          templist.append(number)
​
  for number in range(1, elementcount + 1):
      if number in templist:
          outputlist[check].append(mat[indexcount].pop(0))
          indexcount = len(mat) - 1
          check += 1
      else:
          outputlist[check].append(mat[indexcount].pop(0))
          indexcount -= 1
​
  return outputlist

