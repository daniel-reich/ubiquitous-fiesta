
def pilish_string(txt):
  pi = "314159265358979"
  ret = []
  for i in pi:
    if txt!="":
      if len(txt)>=int(i):
        ret.append(txt[:int(i)])
        txt = txt[int(i):]
      else:
        txt+=txt[-1]*(int(i)-len(txt))
        ret.append(txt)
        txt=''
  return ' '.join(ret)

