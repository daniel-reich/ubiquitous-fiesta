
def lychrel(n):
  test = n
  track = 0
  while True:
    if str(test) == str(test)[::-1]:
      return track
    if track == 500:
      return True
    test += int(str(test)[::-1])
    track  += 1

