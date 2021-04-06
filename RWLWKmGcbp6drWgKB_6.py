
def chosen_wine(wines):
  if len(wines) == 0:
    return None
  elif len(wines) > 1:
    return [x["name"] for x in wines if x["price"] == sorted([item["price"] for item in wines])[1]][0]
  else:
    return wines[0]["name"]

