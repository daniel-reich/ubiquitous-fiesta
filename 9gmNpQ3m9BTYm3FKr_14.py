
def lucky_seven(lst):
  for i in range(len(lst)):
    for j in range(i, len(lst)):
      for z in range(j, len(lst)):
        if i != j and i != z and j != z:
          if lst[i] + lst[j] + lst[z] == 7:
            return True
  return False

