
def column_chart(productA, productB, target):
  ret = []
  maxLen = max(target);
  ret.append((" "*len(str(maxLen))) + " | Mo Tu We Th Fr Sa Su |")
  template = "c | v v v v v v v |"
  for i in range(10,maxLen+20,10):
    tmp = "";cnt=0
    for j in template:
      if j == "c":
        tmp += str(i)
      elif j == "v":
        if productA[cnt] >= i:
          tmp += "++"
        elif productA[cnt]+productB[cnt] >= i:
          tmp += "**"
        elif target[cnt]+10 == i:
          tmp += "__"
        else:
          tmp += "  "
        cnt+=1
      else:
        tmp += j
    ret.append(tmp + "\n");
  final = ""
  for i in range(len(ret)-1,-1,-1):
    final += ret[i]
  
  return final

