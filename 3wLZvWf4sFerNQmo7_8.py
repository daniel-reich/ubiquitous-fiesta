
def neutralise(s1, s2):
  output  = ""
  
  for x in range(len(s1)):
    if s1[x] == s2[x]:
      if s1[x] == "-":
        output = output + "-"
      else:
        output = output + "+"
    else:
      output = output + "0"
  
  return output

