
def trouble(num1, num2):
  numlst1, numlst2 = list(str(num1)), list(str(num2))
  for i in range(len(numlst1)-2):
    if numlst1[i] == numlst1[i+1] == numlst1[i+2]:
      for j in range(len(numlst2)-1):
        if numlst2[j] == numlst2[j+1] == numlst1[i]:
          return True
        else: 
          continue
    else:
      continue
  return False

