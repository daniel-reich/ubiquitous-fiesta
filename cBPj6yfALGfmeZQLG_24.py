
def vertical_txt(txt):
  text = txt.split()
  ans = []
  for i in range(len(sorted(text, key=len)[-1])):
    lst = []
    for j in range(len(text)):
      if i >= len(text[j]):
        lst.append(" ")
      else:
        lst.append(text[j][i])
    ans.append(lst)
  return ans

