
def who_wins_tonight(c, s, p, z):
  return 'Bill' if c//p > s//z else 'Will' if c//p < s//z else 'Tie'

