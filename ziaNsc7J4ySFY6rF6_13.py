
def will_fit(holds, cargo):
  dict = {"S": 50, "M": 100, "L": 200}
  cargo_total = sum([i for i in cargo])
  holds_total = sum([dict[holds[i]] for i in range(len(holds))])
​
  return cargo_total <= holds_total

