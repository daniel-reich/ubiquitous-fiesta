
def will_fit(holds, cargo):
​
  holds_size = []
  for hold in holds:
    if hold == 'S':
      holds_size.append(50)
    elif hold == 'M':
      holds_size.append(100)
    else:
      holds_size.append(200)
      
  for i in range(len(cargo)):
    current_space = holds_size[:]
    for j in range(len(holds_size)):
      if cargo[i] <= holds_size[j]:
        holds_size[j] -= cargo[i]
        break
    flag = True
    for j in range(len(holds_size)):
      if holds_size[j] != current_space[j]:
        flag = False
    if flag == True:
      return False
  return True

