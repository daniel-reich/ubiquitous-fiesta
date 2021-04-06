
def news_at_ten(txt, n):
  lst = [' '*n]
  for i in range(len(txt)+n):
    if i<len(txt):
      temp = lst[-1][1:]+txt[i]
    else:
      temp = lst[-1][1:]
      temp+=' '*(n-len(temp))
    lst.append(temp)
  return lst

