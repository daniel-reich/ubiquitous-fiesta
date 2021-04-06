
def skip_the_sugar(drinks):
  if "cola" in drinks and "fanta" in drinks:
    drinks.remove("cola")
    drinks.remove("fanta")
    return drinks
  elif "cola" in drinks:
    drinks.remove("cola")
    return drinks
  elif "fanta" in drinks:
    drinks.remove("fanta")
    return drinks
  else:
    return drinks

