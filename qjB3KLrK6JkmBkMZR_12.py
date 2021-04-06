
def can_capture(queens):
  me = [ord(c) for c in queens[0]]
  you = [ord(c) for c in queens[1]]
  return True if me[0] == you[0] or me[1] == you[1] else abs(me[0] - you[0]) == abs(me[1] - you[1])

