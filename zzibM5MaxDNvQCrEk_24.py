
def will_fit(holds, cargo):
  def check_cap(size):
    if size == "S":
      cap = 50
    if size == "M":
      cap = 100
    if size == "L":
      cap = 200
    return cap
  for i in range(len(holds)):
    car_cap = check_cap(holds[i])
    if car_cap < cargo[i]:
      return False
  return True

