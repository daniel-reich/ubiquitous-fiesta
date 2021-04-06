
def deadly_virus(persons, n):
  for hours in range(n):
      coordinates = []
      for sublistindex in range(len(persons)):
          if "V" in persons[sublistindex]:
              for position in range(len(persons[sublistindex])):
                  if persons[sublistindex][position] == "V":
                      coordinates.append([sublistindex, position])
​
      for coordpair in coordinates:
          try:
              if coordpair[0] == 0:
                  persons[coordpair[0] + 1][coordpair[1]] = "V"
              else:
                  persons[coordpair[0] - 1][coordpair[1]] = "V"
                  persons[coordpair[0] + 1][coordpair[1]] = "V"
              if coordpair[1] == 0:
                  persons[coordpair[0]][coordpair[1] + 1] = "V"
              else:
                  persons[coordpair[0]][coordpair[1] - 1] = "V"
                  persons[coordpair[0]][coordpair[1] + 1] = "V"
          except:
              print("wrong")
​
  return persons

