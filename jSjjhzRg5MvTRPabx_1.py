
def sentence(w):
  c=[('an 'if i[0]in"aeiuo"else'a ')+i for i in w];c=[i+',' if s<len(c)-2 else 'and '+i+'.' if s == len(c)-1 else i for s,i in enumerate(c)]
  return " ".join(c).capitalize()

