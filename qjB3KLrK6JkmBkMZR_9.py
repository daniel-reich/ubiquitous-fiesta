
def can_capture(queens):
  q1, q2 = queens[0], queens[1]
  if q1[0] == q2[0] or q1[1] == q2[1]:
    return True
  elif abs(ord(q1[0]) - ord(q2[0])) == abs(int(q1[1]) - int(q2[1])):
    return True
  return False

