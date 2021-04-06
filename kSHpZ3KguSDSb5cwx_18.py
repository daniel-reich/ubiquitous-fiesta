
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
  lst =  []
  if not pin.isnumeric() or len(pin) != 4:
    return "Invalid input."
    
  pin_lst = [letter for letter in pin]
  for i in range(0,len(pin_lst)):
    if int(pin_lst[i])+i < len(moves):
      lst.append(moves[int(pin_lst[i])+i])
    else:
      lst.append(moves[int(pin_lst[i])+i-len(moves)])
      
  return lst

