
def will_fit(holds, cargo):
  for h in holds:
    s = {"S": 50, "M": 100, "L": 200}[h]
    while s - cargo[0] >= 0:
      s -= cargo.pop(0)
      if not cargo:
        return True
  return False

