
def left_rotations(txt):
  new=''
  newls=[]
  lst=','.join(txt+txt[:-1]).split(',')
  ls=[lst[i:i+len(txt)] for i in range(len(txt))]
  for i in ls:
    for c in i:
      new+=c
    newls.append(new)
    new=''
  return newls
  
def right_rotations(txt):
  l2=left_rotations(txt)
  l2=l2[::-1]
  l2.insert(0,l2[-1])
  return l2[:-1]

