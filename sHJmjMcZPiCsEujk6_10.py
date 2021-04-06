
def pilish_string(txt):
  if not txt: return ''
  pi15, msg = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9], []
  n = pi15.pop(0)
  while len(txt)>n:
    msg.append(txt[:n])
    txt = txt[n:]
    if not pi15: return ' '.join(msg)
    n = pi15.pop(0)
  msg.append(txt.ljust(n,txt[-1]))
  return ' '.join(msg)

