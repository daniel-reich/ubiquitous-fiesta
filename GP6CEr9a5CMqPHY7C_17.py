
def words_to_sentence(words):
  if words == None:
    return ""
  else:
    output = ""
    realwords = [k for k in words if k != None and k != ""]
    for i in range(len(realwords)):
      if realwords[i] != None and realwords[i] != "":
        if i < len(realwords) - 2:
          output = output + realwords[i] + ", "
        elif i == len(realwords) - 2:
          output = output + realwords[i] + " and "
        elif i == len(realwords) - 1:
          output = output + realwords[i]
​
    return output

