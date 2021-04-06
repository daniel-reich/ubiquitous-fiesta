
def column_chart(productA, productB, target):
  maxi = max(target)+10
  result = []
  for i in range(10, maxi+10, 10):
    temp = str(i) + " | "
    for j in range(7):
      if productA[j] >= i: temp += "++ "
      elif (productB[j] + productA[j]) >= i: temp += "** "
      elif target[j]+10 == i: temp += "__ "
      else: temp += "   "
    temp += "|" 
    result = [temp] + result
  result.append("   | Mo Tu We Th Fr Sa Su |")
  return "\n".join(result)

