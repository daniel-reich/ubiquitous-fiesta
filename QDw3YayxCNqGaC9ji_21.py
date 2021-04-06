
def make_change(c):
  quarters, c = divmod(c, 25)
  dimes, c = divmod(c, 10)
  nickels, pennies = divmod(c, 5)
  return {'q':quarters,'d':dimes,'n':nickels,'p':pennies}

