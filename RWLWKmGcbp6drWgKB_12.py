
def chosen_wine(w):
  if len(w)==1: return w[0]["name"]
  return None if not w else sorted([i["price"], i["name"]] for i in w)[1][-1]

