
def straight_digital(number):
  if number < 100:
    return "Not Straight"
  seq = list(str(number))
  new_list = []
  for i in range(len(seq[:-1])):
    new_list.append(int(seq[i + 1]) - int(seq[i]))
  if len(set(new_list)) == 1:
    if list(set(new_list))[0] == 0:
      return "Trivial Straight"
    return new_list[0]
  else:
    return "Not Straight"

