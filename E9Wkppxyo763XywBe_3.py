
def binary_clock(time):
  time = time.replace(":", "")
  grid = []
  for i in range(0, len(time)):
    grid.append(pattern(time[i], i+1))
  return convert(grid)
​
def pattern(number, index):
  if index == 1:
    dict = {
    "0" : "00  ",
    "1" : "10  ",
    "2" : "01  "
    }
    return dict[number]
  elif index == 2 or index == 4 or index == 6:
    dict = {
    "0" : "0000",
    "1" : "1000",
    "2" : "0100",
    "3" : "1100",
    "4" : "0010",
    "5" : "1010",
    "6" : "0110",
    "7" : "1110",
    "8" : "0001",
    "9" : "1001"
    }
    return dict[number]
  elif index == 3 or index == 5:
    dict = {
    "0" : "000 ",
    "1" : "100 ",
    "2" : "010 ",
    "3" : "110 ",
    "4" : "001 ",
    "5" : "101 "
    }
    return dict[number]
​
def convert(grid):
  grid_temp = []
  word = ""
  for i in range(4-1, -1, -1):
    word = word + grid[0][i] + grid[1][i] + grid[2][i] + grid[3][i] + grid[4][i] + grid[5][i]
    grid_temp.append(word)
    word = ""
  return grid_temp

