
def will_fit(holds, cargo):
  holds_size = {
        "S": 50,
        "M": 100,
        "L": 200
    }
  return sum(holds_size[x] for x in holds) >= sum(cargo)

