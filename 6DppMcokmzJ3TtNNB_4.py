
def true_alphabetic(txt):
  space = [i for i in range(len(txt)) if txt[i]==" "]
  soup = sorted([i for i in txt if i.isalpha()])
  for i in space:
    soup.insert(i," ")
  return "".join(soup)

