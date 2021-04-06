
def safecracker(start, increments):
  status = []
  for i, ele in enumerate(increments):
    if i % 2: start = start + ele     
    else: start = start - ele 
    if start < 0: start += 100
    elif start > 99: start -= 100
    status.append(start)  
  return status

