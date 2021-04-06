
def check_score(s):
  scores = {
    '#': 5,
    'O': 3,
    'X': 1,
    '!': -1,
    '!!': -3,
    '!!!': -5,
  }
  return max(0, 
    sum(
      scores[char] 
      for row in s
      for char in row
    )
  )

