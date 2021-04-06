
def split_bunches(bunches):
  # { name: "currants", quantity: 1 },
  # { name: "grapes", quantity: 2 },
  # { name: "bananas", quantity: 2 }
  # ->
  # { name: "currants", quantity: 1},
  # { name: "grapes", quantity: 1 },
  # { name: "grapes", quantity: 1 },
  # { name: "bananas", quantity: 1 },
  # { name: "bananas", quantity: 1 }
  total = []
  for bunch in bunches:
    if bunch["quantity"] == 1:
      total.append({ "name": bunch["name"], "quantity": 1})
    else:
      i = 1
      while i <= bunch["quantity"]:
        total.append({ "name": bunch["name"], "quantity": 1})
        i += 1
  return total

