
def can_capture(queens):
  letters = ["A","B","C","D","E","F","G","H"]
  nums = ["1","2","3","4","5","6","7","8"]
  
  diff_l = abs(letters.index(queens[0][0]) - letters.index(queens[1][0]))
  diff_n = abs(nums.index(queens[0][1]) - nums.index(queens[1][1]))
  if diff_l == 0 or diff_n == 0:
    return True
  return diff_l == diff_n

