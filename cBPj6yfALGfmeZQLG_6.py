
def vertical_txt(txt):
  txtlst = txt.split()
  m = max(len(w) for w in txtlst)
  res = []
  for i,w in enumerate(txtlst):
    tmp = []
    for j in range(m):
      tmp.append(w[j] if j < len(w) else ' ')
    res.append(tmp)
  return list(map(list,zip(*res)))

