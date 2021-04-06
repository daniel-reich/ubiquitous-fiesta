
def switcheroo(txt):
  init=[]
  for word in txt.split(" "):
    if(word.endswith("nts") or word.endswith("nts,") or word.endswith("nts!") or word.endswith("nts...")):
      x=word.replace("nts", "nce")
      init.append(x)
    elif(word.endswith("nce") or word.endswith("nce.") or word.endswith("nce!") or word.endswith("nce...")):
      y=word.replace("nce", "nts")
      init.append(y)
    else:
      init.append(word)
  result=""
  for x in init:
    result+=(x+" ")
  return result[0:len(result)-1]

