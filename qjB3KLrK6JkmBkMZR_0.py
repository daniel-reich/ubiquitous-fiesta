
def can_capture(queens):
  samefile = queens[0][0] == queens[1][0]
  samerank = queens[0][1] == queens[1][1]
  samediagonal = abs(ord(queens[0][0]) - ord(queens[1][0])) == abs(int(queens[0][1]) - int(queens[1][1]))
  return samefile or samerank or samediagonal

