
import math
​
​
# recursive function to find clockwise coordinates of any index given the square size
def clockwise_pos(i, size, depth = 0):
  if size == 1: return [depth, depth]   # base case (reached only with odd sizes)
​
  elif i >= size**2 - (size-2)**2:
    # keep moving to a smaller square until i will fall within its outer edge
    return clockwise_pos(i-(size**2 - (size-2)**2), size-2, depth+1)
​
  else:   
    # determine coordinates based on group, translate based on distance from corner
    if i % 4 == 0: coord = [0,0 + i//4]
    elif (i-1) % 4 == 0: coord = [0 + i//4, size-1]
    elif (i-2) % 4 == 0: coord = [size-1, size-1 - i//4]
    elif (i-3) % 4 == 0: coord = [size-1 - i//4, 0]
    
    # add depth to account for previous layers
    coord[0] += depth
    coord[1] += depth
    return coord
​
​
# main function to encrypt message using clockwise indexing
def clockwise_cipher(message):
  # determine minimum size that will contain message
  size = math.ceil(len(message)**0.5)
  
  # generate square
  square = []
  for y in range(size):
    square.append([])
    for x in range(size):
      square[y].append(" ")
  # fill square using clockwise coordinates
  for i in range(len(message)):
    coord = clockwise_pos(i, size)
    square[coord[0]][coord[1]] = message[i]
  
  # combine square to form encrypted message
  encrypted_message = ""
  for line in square:
    for char in line:
      encrypted_message += char
  return encrypted_message

