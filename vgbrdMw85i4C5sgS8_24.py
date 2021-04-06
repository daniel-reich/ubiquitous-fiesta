
def skip_the_sugar(drinks):
  if "cola" in drinks:
    drinks.remove("cola")
  if "fanta" in drinks:
    drinks.remove("fanta")
  if "cola" or "fanta" not in drinks:
    return drinks

