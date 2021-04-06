
def can_see_stage(seats):
  return all(all((x[i+1] > x[i])for i in range(len(x)-1)) for x in zip(*seats))
    
​
print(can_see_stage([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]))
print(can_see_stage([
  [2, 0, 0], 
  [1, 1, 1], 
  [2, 2, 2]
]))

