
def left_slide(row):
  left_part =  left_collapse(move_to_left(row));
  right_part  = zero_pad_lst(row , left_part);
  return left_part + right_part;
  
def move_to_left(row):
  left_part  = [e for e in row if e != 0 ];
  right_part  = zero_pad_lst(row , left_part);
  return left_part + right_part;
​
def left_collapse(row ):
  if (len(row) < 2 ):
    return row ;
  if (row[0] == row[1]):
    return [row[0]*2] + left_collapse(row[2:]);
  else :
    return [row[0]] + left_collapse(row[1:])
  
def zero_pad_lst(lst , other):
  return [0 for _ in range(0 , len(lst) - len(other))];

