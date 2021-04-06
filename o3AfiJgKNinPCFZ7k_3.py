
def divide_by_n(txt, n):
  return [txt[n*i:n*(i+1)] for i in range(round(len(txt) / n))]

