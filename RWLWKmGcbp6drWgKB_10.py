
def chosen_wine(wines):
  if wines:
    wine_dict = {d['name']:d['price'] for d in wines}
    if len(wine_dict)==1: return list(wine_dict.keys())[0]
    return sorted(wine_dict,key=wine_dict.get)[1]

