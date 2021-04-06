
def encryption(txt):
  new_txt = txt.replace(" ", "")
  L = len(new_txt)
  cols = ((L-1)//round(L**0.5))+1
  return " ".join(["".join([new_txt[i] for i in range(j,L,cols)]) for j in range(cols)])

