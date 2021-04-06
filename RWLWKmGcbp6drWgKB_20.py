
def chosen_wine(wines):
  if len(wines) ==1:
    return wines[0]["name"]
  if len(wines) == 0:
    return None
  X = wines
  Y = []
  for i in X:
    Y.append(i["price"])
  ind = Y.index(min(Y))
  Y[ind] = max(Y)+1  
  z = Y.index(min(Y))
  return wines[z]["name"]

