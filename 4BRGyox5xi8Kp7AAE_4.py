
def chess_board(pole):
  blackfirst = [1,0,1,0,1,0,1,0]
  whitefirst = [0,1,0,1,0,1,0,1]
​
  Chess_map = {'a':blackfirst, 'b':whitefirst,
         'c':blackfirst, 'd':whitefirst,
         'e':blackfirst, 'f':whitefirst,
         'g':blackfirst, 'h':whitefirst,
        }
  code = Chess_map[pole[0]][int(pole[1])-1]
  if code == 1:
    solution = 'black'
  else:
    solution = 'white'
  
  print(solution)
  return solution

