
def chk(arr,tar):
  if any(row.count(tar) == 3 for row in arr):
    return True
  if any(row.count(tar) == 3 for row in zip(*arr)):
    return True
  if all(arr[i][i] == tar for i in range(3)):
    return True
  new_arr = [row[::-1] for row in arr]
  if all(new_arr[i][i] == tar for i in range(3)):
    return True
  return False
​
def tic_tac_toe(inputs):
  if chk(inputs,'X'):
    return "Player 1 wins"
  elif chk(inputs,'O'):
    return "Player 2 wins"
  return "It's a Tie"

