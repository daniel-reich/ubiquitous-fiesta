
def who_wins_tonight(c, s, p, size):
  return 'Tie' if c//p==s//size else ['Will', 'Bill'][c//p>s//size]

