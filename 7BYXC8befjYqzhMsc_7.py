
def classify_rug(pattern):
  horizontally_imperfect = 0
  for i in range(len(pattern)):
    if pattern[i] != pattern[-1-i]:
      horizontally_imperfect += 1
  vertically_imperfect = 0
  for i in pattern:
    for j in range(len(i)):
      if i[j] != i[-1-j]:
        vertically_imperfect += 1
  if horizontally_imperfect > 0 and vertically_imperfect > 0:
    return("imperfect")
  elif horizontally_imperfect == 0 and vertically_imperfect > 0:
    return("horizontally symmetric")
  elif horizontally_imperfect > 0 and vertically_imperfect == 0:
    return("vertically symmetric")
  elif horizontally_imperfect == 0 and vertically_imperfect == 0:
    return("perfect")

