
def chosen_wine(wines):
  try:
    lst = list(map(lambda x: wines[x],range(0,len(wines))))
    lst.sort(key = lambda x: x["price"])
    return lst[1]["name"]
  except IndexError:
    if len(wines) == 1:
      return lst[0]["name"]
    else:
      return None

