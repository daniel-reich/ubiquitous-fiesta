
def bishop(start, end, n):
  if start == end and n>=0:
    return True
  elif start != end and n==0:
    return False
​
  def get_possible_move(point):
​
    start_x = point[0]
    start_y = point[1]
​
    top_right = [chr(ord(start_x) + i) + str(int(start_y) + i) for i in range(1,9) if ord(start_x) + i < 105 and int(start_y) + i < 9]
    down_left = [chr(ord(start_x) - i) + str(int(start_y) - i) for i in range(1,9) if ord(start_x) - i > 96 and int(start_y) - i > 0]
​
    top_left = [chr(ord(start_x) - i) + str(int(start_y) + i) for i in range(1,9) if ord(start_x) - i > 96 and int(start_y) + i < 9]
    down_right = [chr(ord(start_x) + i) + str(int(start_y) - i) for i in range(1, 9) if ord(start_x) - i < 105 and int(start_y) - i > 0]
​
    return top_left + top_right +down_left + down_right
​
  poss_for_start = get_possible_move(start)
  poss_for_end = get_possible_move(end)
​
  if start in poss_for_end or end in poss_for_start and n>0:
    return True
  for i in poss_for_start:
    if i in poss_for_end and n>1:
      return True
  return False

