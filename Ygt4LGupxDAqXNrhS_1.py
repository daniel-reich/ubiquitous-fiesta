
def spotlight_map(grid):
  def in_spot(a, k, d):
    return ((a==0 and (a==k or a==k+1)) or
      (a==len(d)-1 and (a==k or a==k-1)) or (a==k or a==k-1 or a==k+1))
​
  def get_sum(x, y):
    return sum([sum([row[j] for j, col in enumerate(row) if
      in_spot(x, i, row) and in_spot(y, j, grid)])
        for i, row in enumerate(grid)])
​
  return [[get_sum(i, j) for j, col in enumerate(row)] for i, row in enumerate(grid)]

