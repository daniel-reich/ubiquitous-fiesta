
def schoty(frame):
  num=""
  for i in frame:
    c=0
    for j in i:
      if j=="O":
        c+=1
      if j=="-":
        num+=str(c)
        break
  return int(num)

