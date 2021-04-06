
def batting_avg(lst):
  hits, bats = 0, 0
  for game in lst:
    hits += game[0]
    bats += game[1]
  avg = str(round(hits/bats, 3)) + '00'
  return avg[1:5]

