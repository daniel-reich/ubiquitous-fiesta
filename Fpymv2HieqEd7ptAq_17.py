
def split(txt):
  output=[]
  temp=''
  for p in txt:
    temp+=p
    if temp.count('(')==temp.count(')'):
      output.append(temp)
      temp=''
  return output

