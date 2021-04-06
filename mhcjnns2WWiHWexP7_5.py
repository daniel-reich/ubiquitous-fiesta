
def calculate_arrowhead(lst):
  #at the starta we have no movement
  move = ""
  left = 0
  right = 0
  #the list consist in a series of left and right brackets
  for item in lst:
    for i in range(len(item)):
      if item[i] == "<":
        left +=1
      if item[i] == ">":
        right +=1
  if left == right:
    return move
  if left > right:
    return "<" * (left-right)
  if right > left:
    return ">" * (right-left)

