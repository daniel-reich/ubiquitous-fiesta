
def bracket_logic(xp):
  data1=["{","[","<","("]
  data2=["}","]",">",")"]
  buffers=[]
  for i in xp:
    if i in data1:
      buffers.append(i)
    elif i in data2:
      if buffers[-1]==data1[data2.index(i)]:
        buffers.pop(-1)
      else:
        return False
  return True if len(buffers)==0 else False

