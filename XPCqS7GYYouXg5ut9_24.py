
def simplify_sqrt(n):
  done = False
  largest_square = n+1
  while not done:
    largest_square -= 1
    if largest_square**.5 == int(largest_square**.5) or largest_square == 1:
      if n%(largest_square) == 0:
        done = True
  return(largest_square**.5,n/largest_square)

