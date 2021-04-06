
def will_fit(holds, cargo):
  dir_amount = {"S": 50, "M": 100, "L": 200}
  index = 0
  for amount in holds:
    if dir_amount[amount] < cargo[index]:
      return False
    index += 1
  return True

