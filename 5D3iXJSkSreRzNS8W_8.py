
def news_at_ten(txt, n):
  arr = []
  for inst in range(len(txt) + n):
    new_str = ""
    if inst < n:
      for t in range(n-inst):
        new_str += " "
      new_str += txt[0:inst]
    else:
      new_str += txt[inst-n:inst]
    for t in range(n-len(new_str)):
        new_str += " "
    arr.append(new_str)
  new_str = ""
  for t in range(n):
    new_str += " "
  arr.append(new_str)
  return(arr)

