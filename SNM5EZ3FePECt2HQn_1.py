
def profitable_gamble(prob, prize, pay):
  outcome = prob * prize - pay
  if outcome > 0:
    return True
  else:
    return False

