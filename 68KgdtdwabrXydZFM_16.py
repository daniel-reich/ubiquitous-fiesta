
def generation(x, y):
  g = {
    -3: {
      "m": "great grandfather",
      "f": "great grandmother",
    },
    -2: {
      "m": "grandfather",
      "f": "grandmother",
    },
    -1: {
      "m": "father",
      "f": "mother",
    },
    0: {
      "m": "me!",
      "f": "me!",
    },
    1: {
      "m": "son",
      "f": "daughter",
    },
    2: {
      "m": "grandson",
      "f": "granddaughter",
    },
    3: {
      "m": "great grandson",
      "f": "great granddaughter",
    }
  }
  if x == -3 and y == "m":
      return "great grandfather"
  if x == -3 and y == "f":
      return "great grandmother"
  if x == -2 and y == "m":
      return "grandfather"
  if x == -2 and y == "f":
      return "grandmother"
  if x == -1 and y == "m":
      return "father"
  if x == -1 and y == "f":
      return "mother"
  if x == 0 and y == "m":
      return "me!"
  if x == 0 and y == "f":
      return "me!"
  if x == 1 and y == "m":
      return "son"
  if x == 1 and y == "f":
      return "daughter"
  if x == 2 and y == "m":
      return "grandson"
  if x == 2 and y == "f":
      return "granddaughter"
  if x == 3 and y == "m":
      return "great grandson"
  if x == 3 and y == "f":
      return "great granddaughter"
print(generation(1, "f"))

