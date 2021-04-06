
def profitable_gamble(prob, prize, pay):
  a = prob*prize
  if a > pay:
    return True
  return False

