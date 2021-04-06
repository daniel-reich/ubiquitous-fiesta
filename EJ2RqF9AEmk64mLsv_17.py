
def lottery(ticket, win):
  lst = []
  for element in ticket:
    code, number = element
    code = [ord(char) for char in code]
    lst.append(number in code)
  return '{}er!'.format(['Los', 'Winn'][sum(lst) >= win])

