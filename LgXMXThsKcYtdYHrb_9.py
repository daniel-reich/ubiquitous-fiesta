
def split_and_delimit(txt, num, delimiter):
  s = ""
  for i in range(len(txt)):
    s += txt[i] 
    s += delimiter if i+1!=len(txt) and (i+1)%num == 0 else ""
  return s

