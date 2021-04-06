
def chess_board(pole):
  
  pole = pole.upper()
  chess_dict = {}
  alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
  
  for i in range(1, 9):
    for letter in alpha[0::2]:
      string = letter+str(i)
      if i % 2 == 0:
        chess_dict[string] = "white"
      else:
        chess_dict[string] = "black"
        
    for letter in alpha[1::2]:
      string = letter+str(i)
      if i % 2 == 0:
        chess_dict[string] = "black"
      else:
        chess_dict[string] = "white"
  location = chess_dict.get(pole)
  return location

