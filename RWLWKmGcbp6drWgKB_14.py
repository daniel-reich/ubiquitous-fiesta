
def chosen_wine(wines):
  if (len(wines) == 0):
    return None;
  if (len(wines) == 1):
    return wines[0]["name"];
    
  sorted_wines = sorted(wines , key = lambda item : item["price"]);
  return sorted_wines[1]["name"];

