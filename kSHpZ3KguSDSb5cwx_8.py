
moves = ["Shimmy", "Shake", "Pirouette", "Slide", "Box Step", "Headspin", "Dosado", "Pop", "Lock", "Arabesque"]
​
def dance_convert(pin):
  number_of_moves = len(moves)
  invalidInput = "Invalid input."
​
  if len(pin) < 4:
    return invalidInput
​
  try:
    first = int(pin[0]) % number_of_moves
    second = int(pin[1]) + 1 % number_of_moves
    third = (int(pin[2]) + 2) % number_of_moves
    fourth = (int(pin[3]) + 3) % number_of_moves
  except ValueError:
    return invalidInput 
  
  return [moves[first], moves[second], moves[third], moves[fourth]]

