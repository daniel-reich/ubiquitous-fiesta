
def count_towers(towers):
  if towers == "":
    return 0;
  else:
    count = 0
    for i in range(len(towers[-1])):
      for j in range(len(towers[-1][i])):
        if (towers[-1][i][j]) == "#":
          count += 1
    return count / 2

