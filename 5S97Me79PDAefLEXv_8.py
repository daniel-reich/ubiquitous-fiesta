
def lambda_to_def(code):
  a = b = 0
  for i in range(len(code)):
      if code[i]=="=":
          a = i
          break
  for j in range(len(code)-1, 1, -1):
      if code[j]==":" and code[j+1]!="'":
          b = j
          break
  return "def "+code[:a-1]+"("+code[a+9:b]+")"+":\n\treturn"+code[b+1:]

