
def fire(matrix, coordinates):
  abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  nums = "1234565789"
​
  for i in abc and coordinates[0]:
    col = abc.find(i)
    for k in nums and coordinates[1]:
      row = nums.find(k)
      if matrix[col][row] == ".":
        return "splash"
      elif matrix[col][row] == "*":
        return "BOOM"
      else:
        return "Something went wrong...."

