
def will_fit(holds, cargo):
  total_storage = 0
  for i in holds:
    if i == 'L':
      total_storage += 200
    elif i == 'M':
      total_storage += 100
    else:
      total_storage += 50
  required_storage = sum(cargo)
  if total_storage>= required_storage:
    return True
  else:
    return False

