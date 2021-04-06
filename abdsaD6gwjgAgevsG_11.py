
def power_ranger(power, minimum, maximum):
  square = []
  square_list = []
  for number in range(0,maximum+1):
    square = number**power
    if square in range(minimum,maximum+1):
      square_list.append(square)
  print(square_list)
  return(len(square_list))

