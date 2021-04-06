
def holey_sort(lst):
  def holes(num):
    dig_holes = {4: 1, 6: 1, 8: 2, 9: 1, 0: 1}
    digits = [int(i) for i in str(num)]
​
    holes = 0
​
    for digit in digits:
      if digit in dig_holes.keys():
        holes += dig_holes[digit]
    
    return holes
  def sorrt(key, holes):
​
    hole_amounts = sorted(list(holes.keys()))
    srrted = []
    
    for amount in hole_amounts:
      to_add = holes[amount]
      for item in lst:
        if item in to_add:
          srrted.append(item)
    
    return srrted
​
  num_of_holes = {}
​
  for num in lst:
    hole_amount = holes(num)
    if hole_amount not in num_of_holes.keys():
      num_of_holes[hole_amount] = [num]
    else:
      num_of_holes[hole_amount].append(num)
  
  return sorrt(lst, num_of_holes)

