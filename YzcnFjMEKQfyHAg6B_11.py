
def simon_says(lst1, lst2):
  for x in range(len(lst1)):
    try:
      if lst1[x] == lst2[x+1]:
        pass
      else:
        return False
    except:
      pass
  return True

