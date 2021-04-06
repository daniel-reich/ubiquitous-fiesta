
def chosen_wine(wines):
  w = {i["price"]: i["name"] for i in wines}
  return w[sorted(list(w.keys()))[1]] if len(w) > 1 else w[list(w.keys())[0]] if len(w) == 1 else None

