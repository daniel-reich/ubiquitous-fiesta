
def microwave_buttons(time):
  lst = time.split(":")
  time_digits = []
  button_press = 1
    
  for elements in lst:
    for element in elements:
      time_digits.append(int(element))
            
  if time_digits[0]==0 and time_digits[1] == 0 and time_digits[2]==3 and time_digits[3] == 0:
    return button_press + 1
  if time_digits[0]==0 and time_digits[1] == 1 and time_digits[2]==0 and time_digits[3] == 0:
    return button_press + 2
    
  for i in range(len(time_digits)):
    if time_digits[i] != 0:
      return button_press + (len(time_digits)-i)
    
  return button_press

