
def index_of_caps(word):
  result=[]
  for i, c in enumerate(word):
    if "A" <= c <= "Z":
      result.append(i)
  return result

