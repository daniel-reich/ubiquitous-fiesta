
def alphabet_soup(text):
  result=[]
  for i in range(97,97+26):
    for j in text:
      if chr(i) == j:
        result.append(j)
  return ''.join(result)

